from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime

# our main class will be a digital clock, which inherits from the QWidget class
class DigitalClock(QWidget):
    # let's define the constructor first
    def __init__(self):
        super().__init__()
        # we want to create a time label and then a timer
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        # now we can call the UI initializer
        self.initUI()

    def initUI(self):
        # let's create a vbox layout
        vbox = QVBoxLayout()

        # add our label to the widget
        vbox.addWidget(self.time_label)
        # and set the layout inside our clock widget
        self.setLayout(vbox)

        # now we want to center our label
        self.time_label.setAlignment(Qt.AlignCenter)
        # and style it a bit:
        self.time_label.setStyleSheet("font-size: 120px;"
                                      "color: black;")

        # now we need to connect our timer to the update time function
        self.timer.timeout.connect(self.update_time)
        # and we use the start function to update it every second (1000 ms)
        self.timer.start(1000)

    # now we want to define a function to update the time
    def update_time(self):
        current_time = QTime.currentTime()
        self.time_label.setText(current_time.toString("hh:mm:ss AP"))