import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):
	my_signal = qtc.pyqtSignal(str)

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')

		line_edit = qtw.QLineEdit()
		btn_change = qtw.QPushButton('Ok')

		main_layout = qtw.QHBoxLayout(self)
		main_layout.addWidget(line_edit)
		main_layout.addWidget(btn_change)


		# line_edit.textChanged.connect(btn_change.clicked)
		line_edit.textChanged.connect(self.some_slot)
		# btn_change.clicked.connect(self.some_slot)
		btn_change.clicked.connect(self.my_slot)
		# btn_change.my_signal.connect(self.some_slot)

		self.show()


	def my_slot(self):
		self.my_signal.emit('test')
		self.close()

	@qtc.pyqtSlot(str)
	def some_slot(self,data):
		print(data)
		print(type(data))





if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
