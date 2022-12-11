The app.exec_() method is an important part of any PySide6 application, as it allows
 the application to process events and respond to user input. It's typically 
called after the application's GUI has been set up and the window has been 
shown on the screen.

In Python, the @slot decorator is used to define a method as a slot. A slot 
is a special type of method that is called in response to a signal. A signal 
is an event that is emitted by an object to notify other objects that 
something has happened.

Slot methods are an important part of the PySide6 signal and slot mechanism, 
as they provide a way to handle signals and respond to events in your application. 


PySide6 Slots and Signals Documentation 
https://doc.qt.io/qtforpython/tutorials/basictutorial/signals_and_slots.html

While developing interfaces, you can get a real example by the effect of clicking a button: 
the ‘click’ will be the signal, and the slot will be what happens when that button is clicked, 
like closing a window, saving a document, etc.

Signals are emitted by objects when they change their state in a way that may be interesting to other objects.

Slots can be used for receiving signals, but they are also normal member functions. Just as an object 
does not know if anything receives its signals, a slot does not know if it has any signals connected to it.

You can connect as many signals as you want to a single slot, and a signal can be connected to as 
many slots as you need. It is even possible to connect a signal directly to another signal. 
(This will emit the second signal immediately whenever the first is emitted.)

Basics of a button: 

import sys
from PySide6.QtWidgets import QApplication, QPushButton


def function():
    print("The 'function' has been called!")

app = QApplication()
button = QPushButton("Push this button to call function.")
button.clicked.connect(function)
button.show()
sys.exit(app.exec())
