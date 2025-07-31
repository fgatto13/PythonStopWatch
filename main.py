import sys
from PyQt5.QtWidgets import QApplication, QWidget
from stopwatch import Stopwatch

def main():
    app = QApplication(sys.argv)
    window = Stopwatch()
    window.show()
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
