import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setup_UI()

		# ------------------------ connect singnals with slots ----------------------- #
		# on Cancel click = > execute close method
		self.btn_Cansel.clicked.connect(self.close )
		# on OK click = > execute self.on_close()
		self.btn_OK.clicked.connect(self.on_close )

		self.leUserName.textChanged.connect(self.on_text_changed)
		self.leUserName.returnPressed.connect(self.on_return)

		# self.leUserName.cursorPositionChanged.connect(self.on_cursor_change)
		# self.leUserName.textChanged.connect(self.lePassword.setText)

		self.show();

	def setup_UI(self):
		self.setWindowTitle('Signals And Slots')
		self.setGeometry(500, 300, 600, 300)

		# create Form Group Box
		# form_groupbox = self.create_form_groupbox()
		self.create_form_groupbox()

		# create Buttons Layout
		self.create_buttons_layout()

		# create main layout
		main_layout = qtw.QVBoxLayout(self)
		main_layout.addWidget(self.form_groupbox)
		main_layout.addLayout(self.buttons_layout)

	def create_form_groupbox(self):
		self.leUserName = qtw.QLineEdit(self)
		self.lePassword = qtw.QLineEdit(self)

		self.form_groupbox = qtw.QGroupBox('Login Form')
		form_layout = qtw.QFormLayout(self)
		form_layout.addRow('Name:',self.leUserName )
		form_layout.addRow('Password:', self.lePassword)
		self.form_groupbox.setLayout(form_layout)

	def create_buttons_layout(self):
		self.buttons_layout = qtw.QHBoxLayout()
		self.btn_OK = qtw.QPushButton('OK')
		self.btn_Cansel = qtw.QPushButton('Cancel')
		self.buttons_layout.addWidget(self.btn_OK)
		self.buttons_layout.addWidget(self.btn_Cansel)

	def on_close(self):
		# connect btn's click signal with close
		print('Ok button clicked')

	def on_text_changed(self,data):
		# print(data)
		user_name = data
		# if enter is pressed
		# self.lePassword.setText(data)

	def on_cursor_change(self, old, new):
		print(old, new)

	def on_return(self):
		print('jkgjkfdkfd')
		self.lePassword.setText(user_name)




if __name__ == '__main__':
	user_name = ''

	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
