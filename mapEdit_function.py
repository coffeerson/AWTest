from PySide2.QtGui import *
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt, QRect


class MapEditFunction(QWidget):
    def paintEvent(self, event):
        """
                the method paintEvent() is called automatically
                the QPainter class does all the low-level drawing
                coded between its methods begin() and end()
                """
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(Qt.blue)
        rectangle = QRect(10, 20, 80, 60)
        # 绘制矩形区域
        painter.drawRect(rectangle)
        # 填充矩形区域，使用蓝色的刷子
        painter.fillRect(rectangle, QBrush(QColor(Qt.blue)))

        painter.end()

