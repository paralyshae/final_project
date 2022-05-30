import sys
import cv2

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog

from tool import *

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.actionOpen)
        self.show()

    def actionOpen(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/evidence/')
        if fname[0]:
            f = open(fname[0], 'r', errors="ignore")
            print(f.read())
            print(fname)

if __name__=="__main__":    
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

