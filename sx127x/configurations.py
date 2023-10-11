# Copyright 2020 LeMaRiva|tech lemariva.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


# ESP32 TTGO v1.0
DEVICE_CONFIG_ESP32_TTGO = {
    'miso': 19,
    'mosi': 27,
    'ss': 18,
    'sck': 5,
    'dio_0': 26,
    'reset': 14,
    'led': 2,
}

# M5Stack ATOM Matrix
DEVICE_CONFIG_M5STACK_ATOM_MATRIX = {
    'miso': 23,
    'mosi': 19,
    'ss': 22,
    'sck': 33,
    'dio_0': 25,
    'reset': 21,
    'led': 12,
}

# M5Stack & LoRa868 Module
DEVICE_CONFIG_M5STACK_LORA868 = {
    'miso': 19,
    'mosi': 23,
    'ss': 5,
    'sck': 18,
    'dio_0': 26,
    'reset': 36,
    'led': 12,
}


LORA_PARAMETERS_DEFAULT = {
    'frequency': 868E6, 
    'tx_power_level': 2, 
    'signal_bandwidth': 125E3,    
    'spreading_factor': 8,  # 2^6==64, 2^7==128, 2^8==256, ..., 2^12==4096
    'coding_rate': 5,  # 5==4/5, 6==4/6, 7==4/7, 8==4/8
    'preamble_length': 8,
    'implicit_header': False, 
    'sync_word': 0x12, 
    'enable_CRC': False,
    'invert_IQ': False,
}

"""
LoRa configurations, compatible to rf95modem and RH_RF95

https://github.com/gh0st42/rf95modem
https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html

todo: check if message format (4 octets HEADER: (TO, FROM, ID, FLAGS)) is non standard
"""
# default medium range configuration
LORA_PARAMETERS_RH_RF95_bw125cr45sf128 = {
    'frequency': 868.1E6,  # 868.1E6 or 434E6
    'tx_power_level': 2,
    'signal_bandwidth': 125E3,
    'spreading_factor': 7,
    'coding_rate': 5,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': True,
    'invert_IQ': False,
}
# fast + short range configuration
LORA_PARAMETERS_RH_RF95_bw500cr45sf128 = {
    'frequency': 868.1E6,  # 868.1E6 or 434E6
    'tx_power_level': 2,
    'signal_bandwidth': 500E3,
    'spreading_factor': 7,
    'coding_rate': 5,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': True,
    'invert_IQ': False,
}
# slow + long range configuration
LORA_PARAMETERS_RH_RF95_bw31_25cr48sf512 = {
    'frequency': 868.1E6,  # 868.1E6 or 434E6
    'tx_power_level': 2,
    'signal_bandwidth': 31.25E3,
    'spreading_factor': 9,
    'coding_rate': 8,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': True,
    'invert_IQ': False,
}
# slow + long range configuration
LORA_PARAMETERS_RH_RF95_bw125cr48sf4096 = {
    'frequency': 868.1E6,  # 868.1E6 or 434E6
    'tx_power_level': 2,
    'signal_bandwidth': 125E3,
    'spreading_factor': 12,
    'coding_rate': 8,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': True,
    'invert_IQ': False,
}
# slow + long range configuration
LORA_PARAMETERS_RH_RF95_bw125cr45sf2048 = {
    'frequency': 868.1E6,  # 868.1E6 or 434E6
    'tx_power_level': 2,
    'signal_bandwidth': 125E3,
    'spreading_factor': 11,
    'coding_rate': 5,
    'preamble_length': 8,
    'implicit_header': False,
    'sync_word': 0x12,
    'enable_CRC': True,
    'invert_IQ': False,
}
