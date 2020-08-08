# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OptionSelect.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_Toolbar = QFrame(self.centralwidget)
        self.frame_Toolbar.setObjectName(u"frame_Toolbar")
        self.frame_Toolbar.setMaximumSize(QSize(16777215, 45))
        self.frame_Toolbar.setStyleSheet(u"background-color: rgb(128, 142, 149);")
        self.frame_Toolbar.setFrameShape(QFrame.StyledPanel)
        self.frame_Toolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_toolbar = QHBoxLayout(self.frame_Toolbar)
        self.horizontalLayout_toolbar.setSpacing(0)
        self.horizontalLayout_toolbar.setObjectName(u"horizontalLayout_toolbar")
        self.horizontalLayout_toolbar.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_toolbar.addItem(self.horizontalSpacer)

        self.pushButton_maximize = QPushButton(self.frame_Toolbar)
        self.pushButton_maximize.setObjectName(u"pushButton_maximize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_maximize.sizePolicy().hasHeightForWidth())
        self.pushButton_maximize.setSizePolicy(sizePolicy1)
        self.pushButton_maximize.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_toolbar.addWidget(self.pushButton_maximize)

        self.horizontalLayout_toolbar.setStretch(0, 20)

        self.verticalLayout.addWidget(self.frame_Toolbar)

        self.frame_Up = QFrame(self.centralwidget)
        self.frame_Up.setObjectName(u"frame_Up")
        self.frame_Up.setMaximumSize(QSize(16777215, 120))
        self.frame_Up.setStyleSheet(u"background-color: rgb(176, 190, 197);\n"
"font: 75 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(102, 102, 102);\n"
"\n"
"")
        self.frame_Up.setFrameShape(QFrame.StyledPanel)
        self.frame_Up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_Up)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_Up)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_Up)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_Up)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_Up)

        self.frame_Center = QFrame(self.centralwidget)
        self.frame_Center.setObjectName(u"frame_Center")
        self.frame_Center.setStyleSheet(u"background-color: rgb(128, 142, 149);")
        self.frame_Center.setFrameShape(QFrame.StyledPanel)
        self.frame_Center.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_Center)

        self.frame_Down = QFrame(self.centralwidget)
        self.frame_Down.setObjectName(u"frame_Down")
        self.frame_Down.setMaximumSize(QSize(16777215, 120))
        self.frame_Down.setStyleSheet(u"background-color: rgb(176, 190, 197);\n"
"font: 75 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(102, 102, 102);\n"
"")
        self.frame_Down.setFrameShape(QFrame.StyledPanel)
        self.frame_Down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_Down)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_Down)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_Down)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_exit = QPushButton(self.frame_Down)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        sizePolicy2.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_exit)


        self.verticalLayout.addWidget(self.frame_Down)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_exit.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_maximize.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TEST PROJECT EDIT", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"MAP EDIT", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"AUTO TEST", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CONFIGURATION", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi

