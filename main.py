import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import MainWindowsLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w_Main = QMainWindow()
    ui = MainWindowsLayout.Ui_MainWindow()
    ui.setupUi(w_Main)
    w_Main.show()

    sys.exit(app.exec_())
