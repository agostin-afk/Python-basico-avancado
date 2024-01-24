import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import ICON_FILE


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.adjustFixedSize()
    icon = QIcon(str(ICON_FILE))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()