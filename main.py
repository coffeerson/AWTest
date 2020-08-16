import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from optionSelect_function import *
from mapEdit_function import *


class OptionSelect(QMainWindow):
    def __init__(self):
        # -->从文件中加载UI定义
        # -->从 UI 定义中动态 创建一个相应的窗口对象#
        # -->注意：里面的控件对象也成为窗口对象的属性了
        # -->比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('UI\\OptionSelect.ui')
        OptionSelectFunctions.ui_definition(self)
        self.ui.show()


class MapEdit(QWidget):
    def __init__(self):
        # ui_file = QtCore.QFile('UI\\MapEdit.ui')
        # ui_file.open(QtCore.QFile.ReadOnly)

        # -->从文件中加载UI定义
        # -->从 UI 定义中动态 创建一个相应的窗口对象#
        # -->注意：里面的控件对象也成为窗口对象的属性了
        # -->比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('UI\\MapEdit.ui')
        MapEditFunction.waferPainter(self)
        self.ui.show()


# --》重写QUiLoader，用来加载自定义的widget
class UiLoader(QUiLoader):
    def createWidget(self, class_name, parent=None, name=""):
        if class_name == "MapEditFunction":
            widget = MapEditFunction(parent)
            widget.setObjectName("mapView")
            return widget
        return super(UiLoader, self).createWidget(class_name, parent, name)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # app.setStyle('Fusion')
    pageOptionSelect = OptionSelect()
    pageMapEdit = MapEdit()
    sys.exit(app.exec_())
