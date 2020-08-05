import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w_Main = QWidget()
    w_Main.resize(300, 150)
    w_Main.move(300, 300)
    w_Main.setWindowTitle('AWTest')

    w_Main.show()
    
    sys.exit(app.exec_())
