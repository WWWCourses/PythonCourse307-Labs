import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from registrationForm import RegistrationForm
from loginForm import LoginForm


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Demo App')
		self.setup_UI()

		self.show();

	def setup_UI(self):
		self.btn_register = qtw.QPushButton('Registration')
		self.btn_login = qtw.QPushButton('Login')

		self.main_layout = qtw.QHBoxLayout()
		self.main_layout.addWidget(self.btn_register)
		self.main_layout.addWidget(self.btn_login)

		self.central_widget = qtw.QWidget()
		self.setCentralWidget(self.central_widget)
		self.central_widget.setLayout(self.main_layout)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
