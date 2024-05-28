def reverse_range_inclusive(start, end):
    """
    Returns an inverse range (step -1) including BOTH extremes.
    This breaks the python convention but makes it easier to copy the datasheet.

    Parameters:
    start (int): Start number
    end (int): End number

    Returns:
    range function from start to end decreasing by 1 from start to end.
    """
    return range(start, end-1, -1)


def range_inclusive(start, end):
    """
    Returns a range (step 1) including BOTH extremes.
    This breaks the python convention but makes it easier to copy the datasheet.

    Parameters:
    start (int): Start number
    end (int): End number

    Returns:
    range function from start to end increasing by 1 from start to end.
    """
    return range(start, end+1)


# Dictionary with all the fields for some configuration word and the
# corresponding bit ranges

power_control_fields = {
    "PWR_GStart"           : reverse_range_inclusive(31, 31),
    "PWR_Start"            : reverse_range_inclusive(30, 30),
    "PWR_RST"              : reverse_range_inclusive(29, 29),
    "PWR_18DIS"            : reverse_range_inclusive(18, 18),
    "PWR_25EN_1"           : reverse_range_inclusive(17, 17),
    "PWR_25EN_2"           : reverse_range_inclusive(16, 16),
    "PWR_TOFPET_VCCEN_7"   : reverse_range_inclusive(15, 15),
    "PWR_TOFPET_VCCEN_6"   : reverse_range_inclusive(14, 14),
    "PWR_TOFPET_VCCEN_5"   : reverse_range_inclusive(13, 13),
    "PWR_TOFPET_VCCEN_4"   : reverse_range_inclusive(12, 12),
    "PWR_TOFPET_VCCEN_3"   : reverse_range_inclusive(11, 11),
    "PWR_TOFPET_VCCEN_2"   : reverse_range_inclusive(10, 10),
    "PWR_TOFPET_VCCEN_1"   : reverse_range_inclusive( 9,  9),
    "PWR_TOFPET_VCCEN_0"   : reverse_range_inclusive( 8,  8),
    "PWR_TOFPET_VCC25EN_7" : reverse_range_inclusive( 7,  7),
    "PWR_TOFPET_VCC25EN_6" : reverse_range_inclusive( 6,  6),
    "PWR_TOFPET_VCC25EN_5" : reverse_range_inclusive( 5,  5),
    "PWR_TOFPET_VCC25EN_4" : reverse_range_inclusive( 4,  4),
    "PWR_TOFPET_VCC25EN_3" : reverse_range_inclusive( 3,  3),
    "PWR_TOFPET_VCC25EN_2" : reverse_range_inclusive( 2,  2),
    "PWR_TOFPET_VCC25EN_1" : reverse_range_inclusive( 1,  1),
    "PWR_TOFPET_VCC25EN_0" : reverse_range_inclusive( 0,  0),
}

power_status_fields = {
    "PWR_STATUS_CONF_DONE"        : reverse_range_inclusive(31, 31),
    "PWR_STATUS_CONF_ON"          : reverse_range_inclusive(30, 30),
    "PWR_STATUS_18DIS"            : reverse_range_inclusive(18, 18),
    "PWR_STATUS_25EN_1"           : reverse_range_inclusive(17, 17),
    "PWR_STATUS_25EN_2"           : reverse_range_inclusive(16, 16),
    "PWR_STATUS_TOFPET_VCCEN_7"   : reverse_range_inclusive(15, 15),
    "PWR_STATUS_TOFPET_VCCEN_6"   : reverse_range_inclusive(14, 14),
    "PWR_STATUS_TOFPET_VCCEN_5"   : reverse_range_inclusive(13, 13),
    "PWR_STATUS_TOFPET_VCCEN_4"   : reverse_range_inclusive(12, 12),
    "PWR_STATUS_TOFPET_VCCEN_3"   : reverse_range_inclusive(11, 11),
    "PWR_STATUS_TOFPET_VCCEN_2"   : reverse_range_inclusive(10, 10),
    "PWR_STATUS_TOFPET_VCCEN_1"   : reverse_range_inclusive( 9,  9),
    "PWR_STATUS_TOFPET_VCCEN_0"   : reverse_range_inclusive( 8,  8),
    "PWR_STATUS_TOFPET_VCC25EN_7" : reverse_range_inclusive( 7,  7),
    "PWR_STATUS_TOFPET_VCC25EN_6" : reverse_range_inclusive( 6,  6),
    "PWR_STATUS_TOFPET_VCC25EN_5" : reverse_range_inclusive( 5,  5),
    "PWR_STATUS_TOFPET_VCC25EN_4" : reverse_range_inclusive( 4,  4),
    "PWR_STATUS_TOFPET_VCC25EN_3" : reverse_range_inclusive( 3,  3),
    "PWR_STATUS_TOFPET_VCC25EN_2" : reverse_range_inclusive( 2,  2),
    "PWR_STATUS_TOFPET_VCC25EN_1" : reverse_range_inclusive( 1,  1),
    "PWR_STATUS_TOFPET_VCC25EN_0" : reverse_range_inclusive( 0,  0),
}

leds_status_fields = {
    'LED_7'              : reverse_range_inclusive(7, 7),
    'LED_6'              : reverse_range_inclusive(6, 6),
    'LED_5'              : reverse_range_inclusive(5, 5),
    'LED_4'              : reverse_range_inclusive(4, 4),
    'LED_3'              : reverse_range_inclusive(3, 3),
    'LED_Link_Alignment' : reverse_range_inclusive(2, 0),
}
