import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from main import Ui_MainWindow as View
from tab1 import  Task1
from tab2 import Task2
class MyGUI(QMainWindow, View):
    def __init__(self, parent=None):
        super(MyGUI, self).__init__(parent)
        self.setupUi(self)

        task1 = Task1()
        self.tabWidget.addTab(task1, "ScreenShot")
        task2=Task2()
        self.tabWidget.addTab(task2, "Net")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyGUI()
    w.show()
    app.exec()
