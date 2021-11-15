import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.create_table_ui()
		self.createTableAction()

		self.main_layout = qtw.QVBoxLayout(self)
		self.title = qtw.QLabel('Table Widget Demo')
		self.main_layout.addWidget(self.title)
		self.main_layout.addWidget(self.table)

		style = self.style_sheets()
		self.setStyleSheet(style)
		self.show();

	def create_table_ui(self):
		rows = 5
		cols = 3

		# init table
		self.table = qtw.QTableWidget();
		self.table.setRowCount(rows);
		self.table.setColumnCount(cols);
		self.table.setHorizontalHeaderLabels(['Heading1', 'Heading2', 'Heading3']);

		self.table.setMinimumHeight(cols*100);
		self.table.setMinimumWidth(rows*100);

		self.table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
		self.table.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)

		# set self.table values
		for row in range(rows):
			for col in range(cols):
				self.table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

		# resize cells to content:
		self.table.resizeColumnsToContents();
		self.table.resizeRowsToContents();


		# self.createTableAction()

	def createTableAction(self):
		#  create our custom QActions
		self.add_above_action = qtw.QAction("Add row above", self)
		self.add_above_action.triggered.connect( lambda: self.table.insertRow(self.table.currentRow() ))

	def contextMenuEvent(self, event):
		context_menu = qtw.QMenu(self)
		context_menu.addAction(self.add_above_action)

		#HW: imlement add row below custom action
		context_menu.addAction("Add row bellow")

		# By passing the event's position as argument we ensure that the context menu appears at the expected position.
		context_menu.exec_(event.globalPos())

	def style_sheets(self):
		style  = """
			QLabel:hover{
				background-color: #f99;
			}

			QTableWidget{
				border: 10px solid #3beefa
			}

			horizontalHeader{
				background-color: green
			}


			/* # TODO: why not works */
			QTableWidgetItem{
				border: 1px dotted red
			}

			QHeaderView::section {
				background-color:red
			}

		"""

		return style


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
