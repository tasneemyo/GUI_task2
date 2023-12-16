# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.NetLabel = QLabel(Form)
        self.NetLabel.setObjectName(u"NetLabel")
        self.NetLabel.setGeometry(QRect(0, 0, 500, 500))

        self.illegalLabel = QLabel(Form)
        self.illegalLabel.setObjectName(u"illegalLabel")
        self.illegalLabel.setGeometry(QRect(650, 50, 49, 16))

        self.disruptedLabel = QLabel(Form)
        self.disruptedLabel.setObjectName(u"disruptedLabel")
        self.disruptedLabel.setGeometry(QRect(650, 150, 49, 16))

        self.label1=QLabel(Form)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(520, 50,120, 16))

        self.label2=QLabel(Form)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(520, 150, 120, 16))



        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.NetLabel.setText("")
        self.illegalLabel.setText("")
        self.disruptedLabel.setText("")
        self.label1.setText("")
        self.label2.setText("")

    # retranslateUi

