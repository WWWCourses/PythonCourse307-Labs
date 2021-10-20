import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import uic

generated_class, base_class = uic.loadUiType('./ui/simple_form.ui')
print(generated_class, base_class)


if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)

  w = base_class()
  form = generated_class()
  form.setupUi(w)
  w.show()

  sys.exit(app.exec())

