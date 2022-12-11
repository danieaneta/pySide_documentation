import sys
from PySide6.QtWidgets import QApplication, QPushButton


def function():
    print("The 'function' has been called!")

app = QApplication()
button = QPushButton("Push this button to call function.")
button.clicked.connect(function)
button.show()
sys.exit(app.exec())
