# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(702, 474)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Paginas = QStackedWidget(self.centralwidget)
        self.Paginas.setObjectName(u"Paginas")
        self.Paginas.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEditID = QLineEdit(self.page)
        self.lineEditID.setObjectName(u"lineEditID")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditID.sizePolicy().hasHeightForWidth())
        self.lineEditID.setSizePolicy(sizePolicy)
        self.lineEditID.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.lineEditID, 3, 0, 1, 1)

        self.Pagar = QPushButton(self.page)
        self.Pagar.setObjectName(u"Pagar")

        self.gridLayout_2.addWidget(self.Pagar, 5, 3, 1, 1)

        self.labelProducto = QLabel(self.page)
        self.labelProducto.setObjectName(u"labelProducto")

        self.gridLayout_2.addWidget(self.labelProducto, 2, 0, 1, 1)

        self.framePrincipal = QFrame(self.page)
        self.framePrincipal.setObjectName(u"framePrincipal")
        self.framePrincipal.setFrameShape(QFrame.StyledPanel)
        self.framePrincipal.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.framePrincipal)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollAreaPrincipal = QScrollArea(self.framePrincipal)
        self.scrollAreaPrincipal.setObjectName(u"scrollAreaPrincipal")
        self.scrollAreaPrincipal.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 522, 252))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayoutPrincipal = QGridLayout()
        self.gridLayoutPrincipal.setObjectName(u"gridLayoutPrincipal")

        self.gridLayout_4.addLayout(self.gridLayoutPrincipal, 0, 0, 1, 1)

        self.scrollAreaPrincipal.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollAreaPrincipal, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.framePrincipal, 1, 0, 1, 1)

        self.Agregar = QPushButton(self.page)
        self.Agregar.setObjectName(u"Agregar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Agregar.sizePolicy().hasHeightForWidth())
        self.Agregar.setSizePolicy(sizePolicy1)
        self.Agregar.setMaximumSize(QSize(560, 10777025))

        self.gridLayout_2.addWidget(self.Agregar, 5, 0, 1, 1, Qt.AlignLeft)

        self.lineEditBusqueda = QLineEdit(self.page)
        self.lineEditBusqueda.setObjectName(u"lineEditBusqueda")

        self.gridLayout_2.addWidget(self.lineEditBusqueda, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.page)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_2.addWidget(self.spinBox, 5, 1, 1, 1)

        self.BotonCarro = QPushButton(self.page)
        self.BotonCarro.setObjectName(u"BotonCarro")

        self.gridLayout_2.addWidget(self.BotonCarro, 1, 3, 1, 1)

        self.Paginas.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_5 = QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.framePago = QFrame(self.page_2)
        self.framePago.setObjectName(u"framePago")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.framePago.sizePolicy().hasHeightForWidth())
        self.framePago.setSizePolicy(sizePolicy2)
        self.framePago.setFrameShape(QFrame.StyledPanel)
        self.framePago.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.framePago)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollAreaPago = QScrollArea(self.framePago)
        self.scrollAreaPago.setObjectName(u"scrollAreaPago")
        self.scrollAreaPago.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 609, 292))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayoutPago = QGridLayout()
        self.gridLayoutPago.setObjectName(u"gridLayoutPago")

        self.gridLayout_7.addLayout(self.gridLayoutPago, 0, 0, 1, 1)

        self.scrollAreaPago.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_6.addWidget(self.scrollAreaPago, 0, 1, 1, 1)

        self.lineEditTotal = QLineEdit(self.framePago)
        self.lineEditTotal.setObjectName(u"lineEditTotal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEditTotal.sizePolicy().hasHeightForWidth())
        self.lineEditTotal.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEditTotal, 1, 1, 1, 1)

        self.labelTotal = QLabel(self.framePago)
        self.labelTotal.setObjectName(u"labelTotal")
        sizePolicy3.setHeightForWidth(self.labelTotal.sizePolicy().hasHeightForWidth())
        self.labelTotal.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.labelTotal, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.framePago, 5, 0, 1, 5)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.PagarDefinitivo = QPushButton(self.page_2)
        self.PagarDefinitivo.setObjectName(u"PagarDefinitivo")

        self.gridLayout_5.addWidget(self.PagarDefinitivo, 0, 4, 1, 1)

        self.pushButtonClientes = QPushButton(self.page_2)
        self.pushButtonClientes.setObjectName(u"pushButtonClientes")

        self.gridLayout_5.addWidget(self.pushButtonClientes, 0, 3, 1, 1)

        self.pushButtonCompras = QPushButton(self.page_2)
        self.pushButtonCompras.setObjectName(u"pushButtonCompras")

        self.gridLayout_5.addWidget(self.pushButtonCompras, 0, 2, 1, 1)

        self.lineEditRFC = QLineEdit(self.page_2)
        self.lineEditRFC.setObjectName(u"lineEditRFC")
        self.lineEditRFC.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEditRFC.sizePolicy().hasHeightForWidth())
        self.lineEditRFC.setSizePolicy(sizePolicy3)

        self.gridLayout_5.addWidget(self.lineEditRFC, 2, 0, 1, 1)

        self.Paginas.addWidget(self.page_2)

        self.gridLayout.addWidget(self.Paginas, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 702, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Muebler\u00eda", None))
        self.Pagar.setText(QCoreApplication.translate("MainWindow", u"Pagar", None))
        self.labelProducto.setText(QCoreApplication.translate("MainWindow", u"Id Producto:", None))
        self.Agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.lineEditBusqueda.setInputMask("")
        self.lineEditBusqueda.setText("")
        self.BotonCarro.setText(QCoreApplication.translate("MainWindow", u"Carrito", None))
        self.labelTotal.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RFC", None))
        self.PagarDefinitivo.setText(QCoreApplication.translate("MainWindow", u"Pagar", None))
        self.pushButtonClientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.pushButtonCompras.setText(QCoreApplication.translate("MainWindow", u"Lista Compras", None))
    # retranslateUi

