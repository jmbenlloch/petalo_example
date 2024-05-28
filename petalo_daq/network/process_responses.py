import numpy as np
from   bitarray import bitarray
from   datetime import datetime

from .. gui.types        import LogError
from .. io.utils         import read_bitarray_slice
from .. io.utils         import load_bitarray_config

from .. gui.widget_data  import power_status_data
from .. gui.widget_data  import leds_status_data

from .. io.config_params import power_status_fields
from .. io.config_params import leds_status_fields

from .  commands     import status_codes


def power_regulator_status(window, cmd, params):
    register, value = params
    value_bitarray = convert_int32_to_bitarray(value)

    load_bitarray_config(window, value_bitarray, power_status_fields, power_status_data)


def leds_status(window, cmd, params):
    register, value = params
    value_bitarray = convert_int32_to_bitarray(value)

    load_bitarray_config(window, value_bitarray, leds_status_fields, leds_status_data)


def check_connection(window, cmd, params):
    status = params[0]

    if status == status_codes.STA_CONNECTION_ACCEPT.value:
        window.checkBox_Connected.setChecked(True)
    else:
        window.checkBox_Connected.setChecked(False)

def convert_int32_to_bitarray(value):
    value_binary_str = '{:032b}'.format(value)
    value_bitarray = bitarray(value_binary_str[::-1])
    return value_bitarray
