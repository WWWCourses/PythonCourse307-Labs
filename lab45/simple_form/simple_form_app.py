import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from simple_form_ui import Ui_Form


class MainWindow(qtw.QWidget, Ui_Form):

  def __init__(self , *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

    self.setWindowTitle('')
    self.le_Password.setEchoMode(2)

    self.show();



if __name__ == '__main__':
  app = qtw.QApplication(sys.argv);

  window = MainWindow()

  sys.exit(app.exec_())
