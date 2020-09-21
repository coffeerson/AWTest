import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine("UI\\MapEdit.qml")

    # -->获取根组件，如果没有这一行，会导致 “Internal C++ object (PySide2.QtCore.QObject) already deleted.“ 错误
    rootObj = engine.rootObjects()[0]

    # -->获取objectName为test的组件
    testObject = rootObj.findChild(QObject, "test")
    # -->修改该组件的参数
    testObject.setProperty("width", 100)

    sys.exit(app.exec_())
