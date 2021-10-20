from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import sys
from ui.simple_form import Ui_Form


class MainWindow(qtw.QWidget, Ui_Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# --------------------------- your code starts here -------------------------- #
		form = Ui_Form()
		form.setupUi(self)
		# form.le_Password.setEchoMode(2)

		# ---------------------------- your code ends here --------------------------- #
		self.show();


if __name__ == '__main__':
  app = qtw.QApplication(sys.argv);

  window = MainWindow()

  sys.exit(app.exec_())
