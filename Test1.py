from PyQt5 import QtWidgets, QtGui
from design import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.label.setText('Hello4!')
        self.ui.label.setFont(QtGui.QFont('SansSerif', 25)) 
        self.ui.label.setFixedHeight(50)

 
 

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
