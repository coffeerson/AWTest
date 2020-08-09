
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtUiTools import QUiLoader
from ui_function import *


class OptionSelect(QMainWindow):
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象#
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('UI\OptionSelect.ui')
        UiFunctions.ui_definition(self)
        self.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    frontPageWindows = OptionSelect()

    sys.exit(app.exec_())