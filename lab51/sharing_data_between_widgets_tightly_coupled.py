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

		# connect signals:
		self.btn_change.clicked.connect(self.on_change)

		self.show()

	def on_change(self):
		self.form = FormWindow(self.label.text())
		self.form.btn_submit.clicked.connect(self.on_form_text_changed)

		self.form.show()
		# self.form.edit.setText(self.label.text())

	def on_form_text_changed(self):
		self.label.setText(self.form.edit.text())




class FormWindow(qtw.QWidget):

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




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())