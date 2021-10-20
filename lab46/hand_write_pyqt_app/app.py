import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MyWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):

		super().__init__(**kwargs)
		# --------------------------- your code starts here -------------------------- #
		print(f'Arg is {args[0]} ')
		# ---------------------------- your code ends here --------------------------- #
		self.show();

	# create your methods here
if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MyWindow(3, cursor=qtc.Qt.WaitCursor, windowTitle="Hello")
	# window.setWindowTitle("My App")

	sys.exit(app.exec_())