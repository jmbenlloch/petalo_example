from .  commands import commands       as cmd
from .  commands import status_codes   as status
from .  commands import register_tuple

from . process_responses import power_regulator_status
from . process_responses import leds_status
from . process_responses import check_connection

from .. gui.types             import LogError


def check_write_response(window, cmd, params):
    status_code = params[0]
    if isinstance(status_code, status):
        raise LogError("{} register error {}".format(cmd.name, status_code.name))


response_functions = {
    cmd.CON_STATUS  : check_connection,
    cmd.SOFT_REG_W_r: check_write_response,
    cmd.HARD_REG_W_r: check_write_response,
    cmd.SOFT_REG_R_r : {
        register_tuple(1, 0): leds_status,
    },
    cmd.HARD_REG_R_r : {
        register_tuple(1, 1): power_regulator_status,
    },
}


def read_network_responses(window):
    while not window.rx_stopper.is_set():
        message = window.rx_queue.get()
        if message:
            response_str = 'Response:\n'
            for key, value in message.items():
                response_str += f'\t{key}: {value}\n'
            print(f'{response_str}\n')

            print("Netword response: ", message)
            try:
                cmd      = message['command']
                register = message['params' ][0]
                fn = response_functions[cmd]
                #  print(cmd, register, fn)
                if isinstance(fn, dict):
                    fn = fn[register]

                # process response
                fn(window, cmd, message['params'])
            except KeyError as e:
                print("Function to process {} not found. ".format(register), e)
            except LogError as e:
                window.update_log_info("", str(e))
