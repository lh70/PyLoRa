from time import sleep
from machine import Pin, SoftSPI
from sx127x import SX127x


# ES32 TTGO v1.0
device_config = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':14,
    'led':2,
}


lora_parameters = {
    'frequency': 868E6,
    'tx_power_level': 2,
    'signal_bandwidth': 125E3,
    'spreading_factor': 8,
    'coding_rate': 5,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': False,
    'invert_IQ': False,
}


device_spi = SoftSPI(baudrate = 10000000,
        polarity = 0, phase = 0, bits = 8, firstbit = SoftSPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)

example = 'receiver'  # 'sender' 'receiver'

if __name__ == '__main__':
    if example == 'sender':
        counter = 0
        print('LoRa Sender')

        while True:
            payload = 'Hello ({0})'.format(counter)
            print("sending packet: \n{} ...".format(payload), end='')
            lora.send(payload.encode())
            print("done\n")

            counter += 1
            sleep(5)
    if example == 'receiver':
        print('LoRa Receiver')

        while True:
            payload = lora.try_receive()
            if payload:
                lora.blink_led()
                print('received packet: \n{}\n'.format(payload.decode()))
