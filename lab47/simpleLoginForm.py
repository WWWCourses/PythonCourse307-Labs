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
		self.lFormTitle = qtw.QLabel("Simple Login Form",self)
		self.lUserName = qtw.QLabel("User name",self)
		self.lPassword = qtw.QLabel("Password",self)

		# create line edits:
		self.leUserName = qtw.QLineEdit(self)
		self.lePassword = qtw.QLineEdit(self)

		# self.QHBoxLayoutDemo()
		# self.QGridLayoutDemo()


		self.show();
	def QGridLayoutDemo(self):
		grid = qtw.QGridLayout(self)
		grid.setHorizontalSpacing(20)
		grid.setVerticalSpacing(20)

		# grid.setRowCount(2)
		# grid.setColumnCount(2)

		grid.addWidget(self.lFormTitle, 0, 0, 1, 2)
		grid.addWidget(self.lUserName, 1, 0)
		grid.addWidget(self.leUserName, 1, 1)
		grid.addWidget(self.lPassword, 2, 0)
		grid.addWidget(self.lePassword, 2, 1)

	def QHBoxLayoutDemo(self,):
		# create Vertical Layout:
		rowsLayout = qtw.QVBoxLayout(self)

		# create horisontal layout for each row and add them into rowsLayout:
		row1Layout = qtw.QHBoxLayout()
		row1Layout.addWidget(self.lFormTitle)

		row2Layout = qtw.QHBoxLayout()
		row2Layout.addWidget(self.lUserName)
		row2Layout.addWidget(self.leUserName)

		row3Layout = qtw.QHBoxLayout()
		row3Layout.addWidget(self.lPassword)
		row3Layout.addWidget(self.lePassword)

		rowsLayout.addLayout(row1Layout, 1)
		rowsLayout.addLayout(row2Layout, 3)
		rowsLayout.addLayout(row3Layout, 3)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()


	sys.exit(app.exec_())
