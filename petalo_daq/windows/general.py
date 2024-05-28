from bitarray  import bitarray

from .. gui.utils        import read_parameters
from .. io.config_params import reverse_range_inclusive

from . register_config           import power_status

from .. gui.types        import power_status_tuple
from .. io.config_params import power_status_fields

from .. io.utils         import insert_bitarray_slice

from .. network.client_commands import build_hw_register_write_command
from .. network.client_commands import build_sw_register_write_command
from .. network.client_commands import build_sw_register_read_command
from .. network.commands        import register_tuple
from .. network.process_responses import convert_int32_to_bitarray


# dispatch
from .. io.utils              import read_bitarray_into_namedtuple
from datetime import datetime


def connect_buttons(window):
    """
    Function to connect each button to the function triggered when the button
    is clicked.

    Parameters
    window (PetaloRunConfigurationGUI): Main application
    """

    window.pushButton_LEDs_read      .clicked.connect(read_leds       (window))


def read_leds(window):
    """
    Function to read the leds status register.
    It reads the values from the GUI fields

    Parameters
    window (PetaloRunConfigurationGUI): Main application

    Returns
    function: To be triggered on click
    """

    def on_click():
        #Build command
        daq_id = 0x0000
        register = register_tuple(group=1, id=0)

        command = build_sw_register_read_command(daq_id, register_group=1, register_id=0)
        window.tx_queue.put(command)

        window.update_log_info("LEDs status sent",
                               "LEDs status command sent")

    return on_click
