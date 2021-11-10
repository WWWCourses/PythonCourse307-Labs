import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Main Window')
		self.setGeometry(300, 200, 800, 600)

		# self.textedit = qtw.QTextEdit()

		# make central widget
		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)
		print( self.centralWidget())

		self.menu_bar()
		self.add_actions()
		self.tool_bar()

		self.show();

	def set_font(self):
		print('Setting font size')

	def show_settings(self):
		print('showig settings')

	def add_actions(self):
		self.file_menu.addAction('Open')
		self.file_menu.addAction('Save')
		self.file_menu.addSeparator()
		quit_action = self.file_menu.addAction('Quit', self.close)

		undo_action = self.edit_menu.addAction('Undo', self.textedit.undo)

		# create a QAction manually
		redo_action = qtw.QAction('Redo', self)
		redo_action.triggered.connect(self.textedit.redo)

		self.help_action = qtw.QAction(self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton),'Help',self)
		self.help_action.triggered.connect( lambda :  self.statusBar().showMessage('Sorry, no help yet!') )


		# Actions, which opens custom dialog
		self.edit_menu.addAction(redo_action)
		self.edit_menu.addAction('Set Font…', self.set_font)
		self.edit_menu.addAction('Settings…', self.show_settings)

	def menu_bar(self):
		# add menu items
		menubar = qtw.QMenuBar()
		self.file_menu = menubar.addMenu('&File')
		self.edit_menu = menubar.addMenu('E&dit')
		self.help_menu = menubar.addMenu('Hel&p')
		self.setMenuBar(menubar)

	def tool_bar(self):
		toolbar = self.addToolBar('File')
		# toolbar = qtw.QToolBar('File')

		toolbar.setMovable(False)
		toolbar.setFloatable(False)
		toolbar.setAllowedAreas(
			qtc.Qt.TopToolBarArea |
			qtc.Qt.BottomToolBarArea
		)

		toolbar.addAction(self.help_action)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
