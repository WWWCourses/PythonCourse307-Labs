import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import lib.db as db


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Simple Login Form')
		self.setGeometry(200,200, 600, 400)

		self.setup_UI()

		self.actions()

		# insert data into 'users' table
		self.cnx = db.make_connection('root', '1234', 'test')

		self.show();

	def setup_UI(self):
		# create form:
		self.leUserName = qtw.QLineEdit()
		self.lePassword = qtw.QLineEdit()

		self.form_layout = qtw.QFormLayout()
		self.form_layout.addRow('Name:', self.leUserName)
		self.form_layout.addRow('Password:', self.lePassword)

		# create buttons
		self.buttons_layout = qtw.QHBoxLayout()
		self.btn_submit = qtw.QPushButton('Submit')
		self.btn_cancel = qtw.QPushButton('Cancel')
		self.buttons_layout.addWidget(self.btn_submit)
		self.buttons_layout.addWidget(self.btn_cancel)

		self.main_layout = qtw.QVBoxLayout(self)
		self.lFormTitle = qtw.QLabel("Simple Login Form",self)
		self.main_layout.addWidget(self.lFormTitle)
		self.main_layout.addLayout(self.form_layout)
		self.main_layout.addLayout(self.buttons_layout)

	def actions(self):
		self.btn_cancel.clicked.connect(self.close)
		self.btn_submit.clicked.connect(self.on_form_submit)

	def on_form_submit(self):
		user_name = self.leUserName.text()
		password = self.lePassword.text()
		print(user_name)
		print(password)

		# ---------------------------- insert data into DB --------------------------- #
		# create cursor object
		cursor = self.cnx.cursor()

		# write SQL
		sql = ('''
				INSERT INTO users
               	(username, password)
               	VALUES (%s, %s)
			   ''')

		# execute query:
		cursor.execute(sql, (user_name,password))

		self.cnx.commit()

		cursor.close()

		self.close()




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()


	sys.exit(app.exec_())
