import sys
import os
import threading
from datetime import datetime
from PyQt5    import QtWidgets
from PyQt5    import uic

import petalo_daq.gui.utils              as gui
import petalo_daq.windows.general        as window_general
import petalo_daq.windows.register_config as window_register

from petalo_daq.gui.widget_data  import power_control_data

from petalo_daq.network.petalo_network import SCK_TXRX
from petalo_daq.network.responses      import read_network_responses
from queue     import Queue, Empty
from threading import Thread, Event


qtCreatorFile = "PETALO_v2.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def connect_server(window):
    localhost = window.textBrowser_Localhost    .toPlainText()
    server    = window.textBrowser_Petalo_server.toPlainText()
    cfg_data = {'port'        : 9116,
                'buffer_size' : 1024,
                'localhost'   : localhost,
                'ext_ip'      : server,
               }

    try:
        window.thread_TXRX  = SCK_TXRX(cfg_data,window.tx_queue,window.rx_queue)
        window.thread_TXRX.daemon = True
        window.thread_TXRX.start()
    except ConnectionRefusedError as e:
        window.update_log_info("Connection error", str(e))


class PetaloRunConfigurationGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, test_mode=False):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Add data to all fields and set default values
        gui.populate_fields(self, power_control_data)

        #Button Calls
        window_general.connect_buttons(self)
        window_register.connect_buttons(self)

        if test_mode:
            self.textBrowser_Localhost    .setText('127.0.0.1')
            self.textBrowser_Petalo_server.setText('127.0.0.1')

        self.tx_queue = Queue()
        self.rx_queue = Queue()
        self.tx_stopper = Event()
        self.rx_stopper = Event()

        self.rx_consumer = threading.Thread(target=read_network_responses, args=(self,))
        self.rx_consumer.daemon = True
        self.rx_consumer.start()

        connect_server(self)

        self.pushButton_Connect.clicked.connect(lambda: connect_server(self))


    def update_log_info(self, status, message):
        """
        Method to write messages in the application log and status fields

        The GUI has two text fields to present the status and log information.
        The first one should be a short message and will be printed in the "current
        status" field. The second one can be as long as needed and will be printed
        in the extended log field.

        Parameters:
        status (string): Message for Current status.
        message (string): Extended log message.

        Returns:
        None: The is no return value
        """

        # Limit size
        text = self.textBrowser.toPlainText()
        nlines = len(text.split('\n'))
        if nlines > 200:
            self.textBrowser.clear()

        self.textBrowser.append(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.textBrowser.append(message + '\n')
        self.Log.setText(status)
        # set scroll to the end
        scrollbar = self.textBrowser.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    print (sys.argv)
    test_mode = False
    if (len(sys.argv) > 1):
        if (sys.argv[1] == '-test'):
            test_mode = True
    window = PetaloRunConfigurationGUI(test_mode=test_mode)
    window.show()
    sys.exit(app.exec_())
