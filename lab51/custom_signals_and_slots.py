import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):
	# cretate custom signal which will cary a string data type data:
	sig_submit = qtc.pyqtSignal(str)

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')

		# self.line_edit = qtw.QLineEdit(self)
		self.btn_change = qtw.QPushButton('Change', self)

		# self.line_edit.textChanged.connect(self.btn_change.clicked)
		self.btn_change.clicked.connect(self.onSubmit)


		self.show();

	@qtc.pyqtSlot(bool)
	def onSubmit(self):
		self.sig_submit.emit('abc')
		self.close()

	@qtc.pyqtSlot(str)
	def on_change(self, text):
		print(text)




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
