import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets

# Create the application object
app = QtWidgets.QApplication([])

# Create a window
window = QtWidgets.QWidget()

# Show the window on the screen
window.show()

# Start the main event loop
app.exec_()

#We create a PySide 6 application using the "QApplication" class, and create a window using the "QWidget" class.
