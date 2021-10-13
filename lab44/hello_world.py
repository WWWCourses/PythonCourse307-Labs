import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QLabel,QPushButton

from UI_tmp import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, *args):
		super(MyWindow,self).__init__()
		self.setupUi(self)



app = QApplication(sys.argv)

window = MyWindow("Title")

print(window)
# exit(0)

window.setWindowTitle('PyQt5 App Works')
window.setGeometry(100, 100, 500, 500)

window.show()
sys.exit(app.exec_())