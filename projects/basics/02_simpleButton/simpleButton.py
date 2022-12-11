import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

#Start by importing PySide6 Classing and Python sys module
#Create a python function that logs the message to the console: 

# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)

# Create a button
button = QPushButton("Click This Button")

# Connect the button to the function
button.clicked.connect(say_hello)

# Show the button
button.show()
# Run the main Qt loop
app.exec()
