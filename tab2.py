from PySide6.QtGui import QMouseEvent 
from design2 import Ui_Form as View
from PySide6.QtWidgets import QWidget
import cv2
from timeit import default_timer as timer
from PySide6.QtGui import *
from PySide6.QtCore import *

class Task2(QWidget,View):
    def __init__(self, parent=None):
        super(Task2, self).__init__(parent)
        self.setupUi(self)
        
        self.illegalCounter=0
        self.disruptedCounter=0
        self.start=0
        self.end=0
        self.doubleClickThreshold = 500
        self.originalImage=cv2.imread("net.png")
        self.originalImage=cv2.resize(self.originalImage,(500,500))
        self.image = QImage(cv2.cvtColor(self.originalImage,cv2.COLOR_BGR2RGB), self.originalImage.shape[1], self.originalImage.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(self.image)
        self.NetLabel.setPixmap(pixmap)

        self.label1.setText("illegal -right click-")
        self.label2.setText("disrupted -left click-")
        self.lastClick = None

        self.illegalLabel.setText(str(self.illegalCounter))
        self.disruptedLabel.setText(str(self.disruptedCounter))
        
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:  #illegal two clicks
       
        self.end=timer()
        # print(f"second {self.start} , {self.end}")
        self.SecondClick(event.x(),event.y())
        
        return super().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        
        if event.button() == Qt.LeftButton:
               self.FirstClick(event.x(),event.y())
        else :
            self.SecondClick(event.x(),event.y())
        
        return super().mousePressEvent(event)
 
    def UpdateImage(self):
        self.originalImage=cv2.resize(self.originalImage,(500,500))
        self.image = QImage(cv2.cvtColor(self.originalImage,cv2.COLOR_BGR2RGB), self.originalImage.shape[1], self.originalImage.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(self.image)
        self.NetLabel.setPixmap(pixmap)
    def FirstClick(self,x,y):
        cv2.line(self.originalImage,(x,y),(x+10,y+15),(255,0,0),2)
        cv2.line(self.originalImage,(x+10,y),(x,y+15),(255,0,0),2)
        self.UpdateImage()
        self.disruptedCounter+=1
        self.disruptedLabel.setText(str(self.disruptedCounter))
    def SecondClick(self,x,y):
        cv2.circle(self.originalImage,(x,y),7,(0,0,255),2)
        self.UpdateImage()
        self.illegalCounter+=1
        self.illegalLabel.setText(str(self.illegalCounter))
        self.doubleClicked=True

