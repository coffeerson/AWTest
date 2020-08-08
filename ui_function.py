from PySide2 import QtCore
from PySide2.QtWidgets import QGraphicsDropShadowEffect

from main import *

GLOBAL_STATE = 0


class UiFunctions(QMainWindow):
    def __init__(self):
        self.ui.shadow = QGraphicsDropShadowEffect(self)
        self.ui = QUiLoader().load('UI\OptionSelect.ui')

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # if not maximized
        if status == 0:
            self.ui.showMaximized()
            GLOBAL_STATE = 1
        else:
            GLOBAL_STATE = 0
            self.ui.showNormal()
            self.ui.resize(self.ui.width() + 1, self.ui.height() + 1)

    def ui_definition(self):
        # remove title bar
        self.ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # set drop shadow window

        self.ui.pushButton_maximize.clicked.connect(lambda: UiFunctions.maximize_restore(self))

    def return_status(self):
        return GLOBAL_STATE
