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
		self.styleTable()

		# resize cells to fit the content:
		# self.resizeColumnsToContents()
		# self.resizeRowsToContents()

		# streach table:
		self.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
		# self.verticalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)

		# set all cells hight
		header = self.verticalHeader()
		header.setDefaultSectionSize(80)
		header.setSectionResizeMode(qtw.QHeaderView.Fixed)

		# set table dimensions:
		self.setMinimumWidth(self.cols*250);
		self.setMinimumHeight(self.rows*70);


		self.setTableActions()

	def setValues(self):
		for row in range(self.rows):
			for col in range(self.cols):
				self.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

	def styleTable(self):
		# read external css file:
		css_filepath = './table_style.css'
		try:
			with open(css_filepath, 'r') as f:
				css = f.read()
		except FileNotFoundError:
			print(f'File ({css_filepath}) not found')
			sys.exit(1)

		# set the stylesheet:
		self.setStyleSheet(css)


	def setTableActions(self):
		self.add_row_above = qtw.QAction('Add row above', self);
		self.add_row_above.triggered.connect(lambda: self.insertRow(self.currentRow()));

		self.add_row_bellow = qtw.QAction('Add row bellow', self);
		self.add_row_bellow.triggered.connect(lambda: self.insertRow(self.currentRow()+1));

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

		layout = qtw.QVBoxLayout();
		table_caption = qtw.QLabel('Just a Simple Table and Styles Demo')
		table_caption.setObjectName('table_caption')

		# we cannot align label in style (text-align:center) is not supported on labels, so must do it here:
		table_caption.setAlignment(qtc.Qt.AlignCenter)

		layout.addWidget(table_caption)
		layout.addWidget(self.table)


		main_widget = qtw.QWidget()
		main_widget.setLayout(layout)

		self.setCentralWidget(main_widget)

		self.applyStyle()
		self.show();

	def applyStyle(self):
		style = """
			QLabel#table_caption{
				font-size: 30px;

				font-weight:bold;
			}

		"""
		self.setStyleSheet(style)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
