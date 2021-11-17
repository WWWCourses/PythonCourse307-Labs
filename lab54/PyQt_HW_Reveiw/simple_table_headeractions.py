import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class SimpleTable(qtw.QTableWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rows = args[0]
		self.cols = args[1]

		# make column labels:
		col_labels = []
		for i in range(self.cols):
			col_labels.append(f'Column {i+1}')
		self.setHorizontalHeaderLabels(col_labels)

		self.setValues()


		self.setTableActions()

	def setValues(self):
		for row in range(self.rows):
			for col in range(self.cols):
				self.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))


	def setTableActions(self):
		self.add_row_above = qtw.QAction('Add row above', self);
		self.add_row_above.triggered.connect(self.add_row_above_handler);

		self.add_row_bellow = qtw.QAction('Add row bellow', self);
		self.add_row_bellow.triggered.connect(lambda: self.insertRow(self.currentRow()+1));

	def add_row_above_handler(self):
		self.insertRow(self.currentRow())

		# focus 1st cell in the inserted row:
		self.setCurrentCell(self.currentRow()-1, 0)

	# overload the contextMenuEvent Qt method:
	def contextMenuEvent(self, event):
		context_menu = qtw.QMenu(self)
		context_menu.addAction(self.add_row_above)
		context_menu.addAction(self.add_row_bellow)
		context_menu.exec_(event.globalPos())


class MainWindow(qtw.QMainWindow):
	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.table = SimpleTable(5,3,self)

		self.setCentralWidget(self.table)
		self.show();


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
