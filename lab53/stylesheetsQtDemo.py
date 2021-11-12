import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('stylesheet demo')
		self.setup_UI()

		self.main_stylesheet()

		# self.setStyleSheet(self.main_sheet)
		self.setStyleSheet(self.main_widget_style)

		self.btn_cancel.clicked.connect(self.close)

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

	def main_stylesheet(self):
		# self.main_sheet = '''
		# 	QLabel{
		# 		color: red;
		# 		border:5px solid blue
		# 	}
		# '''

		with open('./main_style.css', 'r') as f:
			self.main_sheet = f.read()

		self.main_widget_style = """
			QWidget{
				background-image: url('./images/dog-ge68edebc6_640.jpg');

			}
		"""


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
