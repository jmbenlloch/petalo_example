from collections import namedtuple
from .. io import config_params
from enum import auto
from enum import Enum


# Name tuples to store all the parameters related to some particular config
# They are constructed using all the keys stated in config_params.py

power_control_tuple      = namedtuple('power_control'     , config_params.power_control_fields)
power_status_tuple       = namedtuple('power_status'      , config_params.power_status_fields)
leds_status_tuple        = namedtuple('leds_status'       , config_params.leds_status_fields)

class LogError(Exception):
    pass

class CommandDispatcherException(Exception):
    pass


# Command dispatcher types
cmd_response_log = namedtuple('cmd_response_log', ('timestamp', 'cmd'))
