# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.FeedLabel = QLabel(Form)
        self.FeedLabel.setObjectName(u"FeedLabel")
        self.FeedLabel.setGeometry(QRect(0, 35, 400, 400))
        self.ScreenShotLabel = QLabel(Form)
        self.ScreenShotLabel.setObjectName(u"ScreenShotLabel")
        self.ScreenShotLabel.setGeometry(QRect(400, 35, 400, 400))
        self.ScreenShotButton = QPushButton(Form)
        self.ScreenShotButton.setObjectName(u"ScreenShotButton")
        self.ScreenShotButton.setGeometry(QRect(250,450, 300, 50))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.FeedLabel.setText("")
        self.ScreenShotLabel.setText("")
        self.ScreenShotButton.setText(QCoreApplication.translate("Form", u"ScreenShot", None))
    # retranslateUi

