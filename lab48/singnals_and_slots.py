import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Signals And Slots')
		self.setGeometry(500, 300, 800, 600)


		# initilize UI
		self.l_user_name = qtw.QLineEdit()
		self.btn_close = qtw.QPushButton('&Close')

		main_layout = qtw.QHBoxLayout(self)
		main_layout.addWidget(self.l_user_name, 2)
		main_layout.addWidget(self.btn_close, 1)

		# connect signals with slots:
		self.btn_close.clicked.connect(self.close)

		self.show();

	def on_close(self):
		# connect btn's click signal with close
		pass




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
