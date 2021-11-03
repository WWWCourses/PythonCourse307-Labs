import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# from ui.login_form import LoginForm

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My App')

		# ------------------------- create and atach widgets ------------------------- #
		self.label = qtw.QLabel('Initial Text')
		self.btn_change = qtw.QPushButton('change text')

		self.main_layout = qtw.QVBoxLayout()
		self.main_layout.addWidget(self.label)
		self.main_layout.addWidget(self.btn_change)
		self.setLayout(self.main_layout)

		self.show()

		# ---------------------------------- signals --------------------------------- #
		self.btn_change.clicked.connect(self.onChangeClicked)


	def onChangeClicked(self):
		# tightly-coupled demo:
		# self.form_widget = FormWindow()
		# self.form_widget.edit.setText(self.label.text())

		# loosly-coupled approach:
		self.form_widget = FormWindow(self.label.text())
		self.form_widget.sig_submit.connect(self.label.setText)
		self.form_widget.show()


class FormWindow(qtw.QWidget):
	# cretate custom signal which will cary a string data type data:
	sig_submit = qtc.pyqtSignal(str);

	def __init__(self , msg, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My Form')

		# ------------------------- create and atach widgets ------------------------- #
		self.edit = qtw.QLineEdit(msg)
		# self.edit.setText(msg)
		self.btn_submit = qtw.QPushButton('Submit')

		self.setLayout(qtw.QVBoxLayout())
		self.layout().addWidget(self.edit)
		self.layout().addWidget(self.btn_submit)

		# will be shown by parent
		# self.show();

		# ---------------------------------- signals --------------------------------- #
		self.btn_submit.clicked.connect(self.onSubmit)

	@qtc.pyqtSlot(bool)
	def onSubmit(self):
		self.sig_submit.emit(self.edit.text())
		self.close()



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())