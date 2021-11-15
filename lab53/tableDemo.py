import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MyTable(qtw.QWidget):
	def __init(self):
		rows = 5
		cols = 3

		# init table
		table = qtw.QTableWidget(self);
		table.setRowCount(rows);
		table.setColumnCount(cols);
		table.setHorizontalHeaderLabels(['Heading1', 'Heading2', 'Heading3']);

		table.setMinimumHeight(rows*100);
		table.setMinimumWidth(cols*100);

		# set table values
		for row in range(rows):
			for col in range(cols):
				table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

		# resize cells to content:
		table.resizeColumnsToContents();
		table.resizeRowsToContents();


		# self.createTableAction()

		# table.show()

	def createTableAction(self):
		#  create our custom QActions
		self.add_above_action = qtw.QAction("Add row above", self)
		self.add_above_action.triggered.connect( lambda: self.insertRow(self.currentRow() ))

	def contextMenuEvent(self, event):
		context_menu = qtw.QMenu(self)
		context_menu.addAction(self.add_above_action)

		#HW: imlement add row below custom action
		# context_menu.addAction("Add row bellow")

		# By passing the event's position as argument we ensure that the context menu appears at the expected position.
		context_menu.exec_(event.globalPos())

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.table = MyTable()
		self.main_layout = qtw.QVBoxLayout(self)
		print(dir(self.table))
		self.main_layout.addWidget(self.table)

		self.show();




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
