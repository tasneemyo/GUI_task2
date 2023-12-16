from PySide6.QtWidgets import QWidget
#from tab1 import Ui_Form as View
from design1 import Ui_Form as View
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import cv2
class Task1(QWidget, View):
    def __init__(self, parent=None):
        super(Task1, self).__init__(parent)
        self.setupUi(self)
        self.ScreenShotButton.clicked.connect(self.TakeScreenShot)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
        #pass

    def TakeScreenShot(self):
        
        image=self.Worker1.sendFrames()
        #image=cv2.imread("image.png")
        image = QImage(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(image)
        self.ScreenShotLabel.setPixmap(pixmap)
       
        # print(image.shape)
        

class Worker1(QThread):
    ImageUpdate = Signal(QImage)
    ScreenShot=[]
    ScreenShot2=[]
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                self.ScreenShot=frame.copy()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                frame = frame.scaled(640, 480, Qt.KeepAspectRatio)
                self.ScreenShot2=frame.copy()
                self.ImageUpdate.emit(frame)

    def sendFrames(self):
        return self.ScreenShot
            
        
    
    
