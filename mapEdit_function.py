from PySide2.QtGui import *
from PySide2.QtWidgets import QGraphicsScene, QWidget, QGraphicsEllipseItem


# --》重写paintEvent
class MapEditFunction(QWidget):
    def waferPainter(self):
        blackPen = QPen(Qt.black)
        blackPen.setWidth(1)
        blueBrush = QBrush(Qt.blue)
        scene = QGraphicsScene()
        chipNumX = 100
        chipNumY = 100
        canvasWidth = self.ui.mapView.width()
        canvasHeight = self.ui.mapView.height()
        chipWidthX = (canvasWidth - 5) / chipNumX
        chipHeightY = (canvasHeight - 5) / chipNumY
        waferEllipse = QGraphicsEllipseItem()
        scene.addEllipse(0, 0, canvasWidth - 5, canvasHeight - 5, blackPen)
        for numx in range(0, chipNumX):
            for numy in range(0, chipNumY):
                scene.addRect(numx * chipWidthX, numy * chipHeightY, chipWidthX, chipHeightY, blackPen, blueBrush)


        # --》隐藏graphicsView的滚动条
        self.ui.mapView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.mapView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ui.mapView.setScene(scene)
