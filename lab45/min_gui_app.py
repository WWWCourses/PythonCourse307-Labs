# 1. import needed QtWidgets classes
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 2. the main app instance for our application.
app = QApplication(sys.argv)

# 3. Create Qt widget, which will be our main window.
window = QWidget()

# 4. show the window
window.show()

# 5. Start the event loop
app.exec_()

