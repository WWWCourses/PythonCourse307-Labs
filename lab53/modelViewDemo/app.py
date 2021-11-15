import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import csv


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.setupModelView()

		self.show();

	def loadCSVFile(self):
		file_name = "./parts.csv"

		with open(file_name, "r") as csv_f:
			reader = csv.reader(csv_f, delimiter=';')
			header_labels = next(reader)
			self.model.setHorizontalHeaderLabels(header_labels)

			for i, row in enumerate(csv.reader(csv_f,delimiter=';')):
				items = [qtg.QStandardItem(item) for item in row]
				self.model.insertRow(i, items)

	def setupModelView(self):
		# initialize the model
		self.model = qtg.QStandardItemModel()

		# setup table view
		table_view = qtw.QTableView()
		table_view.SelectionMode(3)

		# set up the view to display items in the model
		table_view.setModel(self.model)

		# Set initial row and column values
		self.model.setRowCount(3)
		self.model.setColumnCount(4)

		# load data
		self.loadCSVFile()

		v_box = qtw.QVBoxLayout()
		v_box.addWidget(table_view)
		self.setLayout(v_box)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
