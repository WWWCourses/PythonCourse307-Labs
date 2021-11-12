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

		# set style:
		style = """
			QTextEdit{
				background-image:url('./images/dog-ge68edebc6_640.jpg');
				background-repeat:no-repeat;
				background-position: center center;
				# TODO: check docs
				backgorund-size: 100% 100%;

			}
		"""
		self.setStyleSheet(style)

		self.menu_bar()
		self.add_actions()
		self.tool_bar()
		self.dock_replace()
		self.status_bar()

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
		self.help_action.triggered.connect( lambda :  self.status_bar.showMessage('Sorry, no help yet!', 1000) )


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

	def dock_replace(self):
		dock = qtw.QDockWidget("Replace")
		self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)

		# set dock widget to move and float (but not closeable)
		dock.setFeatures(
			qtw.QDockWidget.DockWidgetMovable |
			qtw.QDockWidget.DockWidgetFloatable |
			qtw.QDockWidget.DockWidgetClosable
		)

		replace_widget = qtw.QWidget()
		replace_widget.setLayout(qtw.QVBoxLayout())
		dock.setWidget(replace_widget)

		self.search_text_input = qtw.QLineEdit(placeholderText='search')
		self.replace_text_input = qtw.QLineEdit(placeholderText='replace')
		search_and_replace_btn = qtw.QPushButton(
			"Search and Replace",
			clicked=self.search_and_replace
			)
		replace_widget.layout().addWidget(self.search_text_input)
		replace_widget.layout().addWidget(self.replace_text_input)
		replace_widget.layout().addWidget(search_and_replace_btn)
		replace_widget.layout().addStretch()

	def status_bar(self):
		self.status_bar = qtw.QStatusBar()
		self.setStatusBar(self.status_bar)

		charcount_label = qtw.QLabel("chars: 0")
		self.textedit.textChanged.connect(
			lambda: charcount_label.setText( "chars: " + str(len(self.textedit.toPlainText())) )
		)
		self.status_bar.addPermanentWidget(charcount_label)

	def search_and_replace(self):
		print('search_and_replace')

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
