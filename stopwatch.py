import os
import sys

from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTime, Qt, QTimer

from digitalClock import DigitalClock

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        # we now want to create all the objects used in the widget
        self.time = QTime(0, 0, 0, 0) # we pass hours, minutes, seconds
        self.timeLabel = QLabel("00:00:00.00", self) # we need it to represent the time
        self.startButton = QPushButton("Start", self)
        self.stopButton = QPushButton("Stop", self)
        self.resetButton = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.clock = DigitalClock()
        # we now need to initialize the UI
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stopwatch')

        # let's define the layout
        vbox = QVBoxLayout()
        # and add our elements
        vbox.addWidget(self.clock)
        vbox.addWidget(self.timeLabel)

        # we now want to set the layout inside the widget:
        self.setLayout(vbox)
        self.timeLabel.setAlignment(Qt.AlignCenter)

        # to horizontally align the buttons, we create a horizontal layout:
        hbox = QHBoxLayout()
        # and add the buttons to it
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.resetButton)
        # finally, let's add the horizontal layout to the vertical layout
        vbox.addLayout(hbox)

        # now for some styling:
        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
            }
            QPushButton {
                font-size: 50px;
                border: 1px solid black;
                border-radius: 10px;
            }
            QPushButton::hover {
                background-color: lightgray;
            }
            QLabel {
                font-size: 120px;
                background-color: #f9f9f9;
                border-radius: 20px;
            }
        """)
        # and set the cursor for the buttons:
        for btn in self.findChildren(QPushButton):
            btn.setCursor(Qt.PointingHandCursor)

        # then we want to load our custom font
        self.load_font()

        # now, we need to connect the click event to an action
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.resetButton.clicked.connect(self.reset)

        # and with the timeout signal, we update the screen
        self.timer.timeout.connect(self.update_display)

    # let's define a couple of methods for the stopwatch:
    def start(self):
        self.timer.start(10)
        self.timeLabel.setStyleSheet("color: green;")
        self.startButton.setDisabled(True)

    def stop(self):
        self.timer.stop()
        self.timeLabel.setStyleSheet("color: red;")
        self.startButton.setDisabled(False)
        self.stopButton.setDisabled(True)

    def reset(self):
        self.timer.stop()
        # we now want to reset the time:
        self.time = QTime(0, 0, 0, 0)
        # and reset the label, using the format_time function
        self.timeLabel.setText(self.format_time(self.time))
        self.timeLabel.setStyleSheet("color: black;")
        self.startButton.setDisabled(False)
        self.stopButton.setDisabled(False)

    # and a method to format our time
    def format_time(self, time):
        # let's create some local variables:
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 # to convert from 3 digits to 2
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    # and to update the display
    def update_display(self):
        self.time = self.time.addMSecs(10) # we update the timer every 10 ms
        self.timeLabel.setText(self.format_time(self.time))

    def load_font(self):
        try:
            if hasattr(sys, '_MEIPASS'):
                # For PyInstaller
                base_path = sys._MEIPASS
            elif getattr(sys, 'frozen', False):
                # Running inside a macOS .app bundle
                base_path = os.path.join(os.path.dirname(sys.executable), "..", "Resources")
            else:
                # Normal execution
                base_path = os.path.dirname(__file__)
            font_path = os.path.abspath(os.path.join(base_path, "fonts", "ds_digital", "DS-DIGIT.TTF"))
            font_id = QFontDatabase.addApplicationFont(font_path)

            # we want to check if the font has been loaded:
            if font_id == -1:
                # if not, it raises an exception
                raise RuntimeError("Failed to load custom font")

            # we then retrieve the family from the db
            families = QFontDatabase.applicationFontFamilies(font_id)
            # and check that the list is not empty
            if not families:
                # if so, we raise an exception
                raise IndexError("No font families returned")
            # otherwise, we set up the font
            my_font = QFont(families[0], 150)
        except (FileNotFoundError, IndexError, RuntimeError, OSError) as e:
            print(e)
            # go back to system font
            my_font = QFont()
            my_font.setPointSize(150)
        self.timeLabel.setFont(my_font)
        self.startButton.setFont(my_font)
        self.stopButton.setFont(my_font)
        self.resetButton.setFont(my_font)
        self.clock.time_label.setFont(my_font)