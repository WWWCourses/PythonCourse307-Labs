import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('PyQt5 App Works')
window.setGeometry(100, 100, 500, 500)

window.show()
sys.exit(app.exec_())