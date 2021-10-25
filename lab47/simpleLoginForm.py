import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Simple Login Form')
		self.setGeometry(200,200, 600, 400)

		# create form labels:
		lFormTitle = qtw.QLabel("Simple Login Form",self)
		lUserName = qtw.QLabel("User name",self)
		lPassword = qtw.QLabel("Password",self)

		lUserName.move(10, 10)
		lPassword.move(10, 40)

		# create line edits:
		leUserName = qtw.QLineEdit(self)
		lePassword = qtw.QLineEdit(self)
		leUserName.move(10, 70)
		lePassword.move(10, 100)



		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
