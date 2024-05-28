from bitarray  import bitarray
import numpy as np

from .. gui.utils         import read_parameters

from .. gui.widget_data   import power_control_data
from .. gui.types         import power_control_tuple
from .. io .config_params import power_control_fields

from .. io.utils         import insert_bitarray_slice

from .. network.client_commands import build_hw_register_write_command
from .. network.client_commands import build_hw_register_read_command
from .. network.commands        import register_tuple


def connect_buttons(window):
    """
    Function to connect each button to the function triggered when the button
    is clicked.

    Parameters
    window (PetaloRunConfigurationGUI): Main application
    """
    window.pushButton_Power_hw_reg.clicked.connect(power_control     (window))
    window.pushButton_Power_status_hw_reg .clicked.connect(power_status(window))


def power_control(window):
    """
    Function to update the power configuration.
    It reads the values from the GUI fields

    Parameters
    window (PetaloRunConfigurationGUI): Main application

    Returns
    function: To be triggered on click
    """

    def on_click():
        power_control_bitarray = bitarray('0'*32)

        power_config = read_parameters(window, power_control_data, power_control_tuple)

        for field, positions in power_control_fields.items():
            #  print(field)
            value = getattr(power_config, field)
            #  print(field, positions, value)
            insert_bitarray_slice(power_control_bitarray, positions, value)

        #Build command
        daq_id = 0x0000
        register = register_tuple(group=1, id=0)
        #  print(power_control_bitarray)
        value = int(power_control_bitarray.to01()[::-1], 2) #reverse bitarray and convert to int in base 2
        #  print(value, hex(value))

        command = build_hw_register_write_command(daq_id, register.group, register.id, value)
        #  print(command)
        # Send command
        window.tx_queue.put(command)

        window.update_log_info("PWR control sent",
                               "Power control register sent")

    return on_click


def power_status(window, verbose=True):
    """
    Function to read the power status register.
    It reads the values from the GUI fields

    Parameters
    window (PetaloRunConfigurationGUI): Main application

    Returns
    function: To be triggered on click
    """

    def on_click():
        #  daq_id = 0
        #  command = build_hw_register_read_command(daq_id, register_group=1, register_id=1)
        #  window.tx_queue.put(command)
        read_hw_status_register(window, register_group=1, register_id=1)

        if verbose:
            window.update_log_info("Power status sent",
                                   "Power status command sent")

    return on_click


def read_hw_status_register(window, register_group, register_id):
    daq_id = 0
    command = build_hw_register_read_command(daq_id, register_group, register_id)
    window.tx_queue.put(command)
