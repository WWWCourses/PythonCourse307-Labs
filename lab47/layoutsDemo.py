import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Layout Demo')

		# create buttons
		btn1 = qtw.QPushButton("One")
		btn2 = qtw.QPushButton("Two")
		btn3 = qtw.QPushButton("Threeeeeeeeeeee")
		btnLogin = qtw.QPushButton("Login")
		btnCancel = qtw.QPushButton("Cancel")

		# create horisontal layout
		hl = qtw.QHBoxLayout(self)
		hl.addWidget(btnLogin)
		hSpacer = qtw.QSpacerItem(200, 20)
		hl.addItem(hSpacer)
		hl.addWidget(btnCancel)



		# hl = qtw.QHBoxLayout()
		# self.setLayout(hl)
		# hl.addWidget(btn1,1)
		# hl.addWidget(btn2,2)
		# hl.addWidget(btn3,3)


		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
