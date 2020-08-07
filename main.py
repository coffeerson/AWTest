import os
import sys

import PySide2
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtCore

from UI import MainWindowsLayout

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w_Main = QMainWindow()
    ui = MainWindowsLayout.Ui_MainWindow()
    ui.setupUi(w_Main)
    w_Main.show()

    sys.exit(app.exec_())
