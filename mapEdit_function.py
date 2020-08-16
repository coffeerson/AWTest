from PySide2.QtGui import *
from PySide2.QtWidgets import QGraphicsScene, QWidget


# --》重写paintEvent
class MapEditFunction(QWidget):
    def waferPainter(self):
        blackPen = QPen(Qt.black)
        blueBrush = QBrush(Qt.blue)
        scene = QGraphicsScene()
        text1 = scene.addText("Hello, world!")
        chipNumX = 3
        chipNumY = 3
        canvasWidth = self.ui.mapView.width()
        canvasHeight = self.ui.mapView.height()
        chipWidthX = canvasWidth/chipNumX
        chipHeightY = canvasHeight/chipNumY
        for numx in range(0, chipNumX):
            for numy in range(0, chipNumY):
                scene.addRect(numx*chipWidthX, numy*chipHeightY, chipWidthX, chipHeightY, blackPen, blueBrush)
        self.ui.mapView.setScene(scene)
