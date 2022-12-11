
import sys
from PySide6.QtWidgets import QApplication, QLabel


# Create the Qt Application
app = QApplication(sys.argv)

#A QLabel is a widget that can present text (simple or rich, like html), and images
label = QLabel("This is the label used with QLabel.")
label.show()
app.exec()
