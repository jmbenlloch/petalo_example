from bitarray import bitarray

# Dictionaries with GUI field names as keys. The values has the following structure:
#  'default' :  Defalt value for the field
#  'values'  : Dictionary with possible values.
#      Keys are the index,
#       'text'  is the label for the GUI,
#       'value' is the actual internal value for that parameter.


power_control_data = {
    "checkBox_PWR_GStart" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_Start" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_RST" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_18DIS" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_25EN_1" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_25EN_2" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCCEN_0" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCCEN_1" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCCEN_2" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCCEN_3" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
},
    "checkBox_PWR_TOFPET_VCCEN_4" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCCEN_5" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCCEN_6" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCCEN_7" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_0" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_1" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_2" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_3" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_4" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_5" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_6" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
    "checkBox_PWR_TOFPET_VCC25EN_7" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('1') },
            True  : {'value' : bitarray('0') },
        },
    },
}

power_status_data = {
    "checkBox_PWR_STATUS_CONF_DONE" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_CONF_ON" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_18DIS" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_25EN_1" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_25EN_2" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_0" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_1" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_2" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_3" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_4" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_5" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_6" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCCEN_7" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_0" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_1" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_2" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_3" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_4" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_5" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_6" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    "checkBox_PWR_STATUS_TOFPET_VCC25EN_7" : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
}

leds_status_data = {
    'checkBox_LED_7' : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    'checkBox_LED_6' : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    'checkBox_LED_5' : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    'checkBox_LED_4' : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    'checkBox_LED_3' : {
        'default' : False,
        'values' : {
            False : {'value' : bitarray('0') },
            True  : {'value' : bitarray('1') },
        },
    },
    'lcdNumber_LED_Link_Alignment' : {
        'default' : False,
        'values' : {
            0 : {'value' : bitarray('000') },
            1 : {'value' : bitarray('001') },
            2 : {'value' : bitarray('010') },
            3 : {'value' : bitarray('011') },
            4 : {'value' : bitarray('100') },
            5 : {'value' : bitarray('101') },
            6 : {'value' : bitarray('110') },
            7 : {'value' : bitarray('111') },
        },
    },
}
