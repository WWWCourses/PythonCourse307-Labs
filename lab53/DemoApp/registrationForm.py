import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import lib.db as db


class RegistrationForm(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		print('RegistrationForm Init')

		self.setWindowTitle('Registraion Form')
		self.setGeometry(300, 300, 400, 200)

		# move window to center
		qt_rect = self.frameGeometry()
		screen_center_point = qtw.QDesktopWidget().availableGeometry().center()
		qt_rect.moveCenter(screen_center_point)
		self.move(qt_rect.topLeft())

		self.setupUI()
		self.setupSignals()

		self.cnx = db.make_connection('root', '1234', 'test')
		# print(self.cnx)

		self.show();

	def setupUI(self):
		# create form layout:
		self.le_user_name = qtw.QLineEdit()
		self.le_password = qtw.QLineEdit()

		form_layout = qtw.QFormLayout()
		form_layout.addRow('Name:',self.le_user_name )
		form_layout.addRow('Password:', self.le_password)

		# create buttons layout:
		self.btn_submit = qtw.QPushButton('Submit')
		self.btn_cancel = qtw.QPushButton('Cancel')
		buttons_layout = qtw.QHBoxLayout()
		buttons_layout.addWidget(self.btn_submit)
		buttons_layout.addWidget(self.btn_cancel)

		# create main layout
		main_layout = qtw.QVBoxLayout(self)
		main_layout.addLayout(form_layout)
		main_layout.addLayout(buttons_layout)

	def setupSignals(self):
		# close windoed on cancel click
		self.btn_cancel.clicked.connect(self.close)

		# get input data on Submit btn press or on password enter:
		self.btn_submit.clicked.connect(self.on_submit)
		self.le_password.returnPressed.connect(self.on_submit)

	def on_submit(self):
		user_name = self.le_user_name.text()
		password = self.le_password.text()
		print(f'UserName: {user_name}')
		print(f'Password: {password}')

		cursor = self.cnx.cursor()

		sql = f"""
			INSERT INTO users (username, password)
			 	VALUES ('{user_name}','{password}');
		"""

		# sql =(
		# 	"INSERT INTO users (username, password) "
		# 	"VALUES (%s, %s)"
		# )
		try:
			# cursor.execute(sql, (user_name, password))
			cursor.execute(sql)
			self.cnx.commit()
		except Exception as err:
			print(f'Error: {err}')
			exit(1)

		infoBox = qtw.QMessageBox()
		infoBox.setIcon(qtw.QMessageBox.Information)
		infoBox.setText('You are now registerd!')
		infoBox.setStandardButtons(qtw.QMessageBox.Ok)
		# infoBox.buttonClicked.connect(lambda i: print(f'Pressed: {i}'))
		infoBox.exec()
		self.close()





if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = RegistrationForm()
	print('Registraion From main')

	sys.exit(app.exec_())
