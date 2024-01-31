import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit,QPushButton
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import ICON_FILE
from display import Display
from infor import Infor


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    display = Display()
    botao1 = QPushButton('botoa 1')
    icon = QIcon(str(ICON_FILE))
    info = Infor('teste')
    window.addWidgetVlayout(info, False)
    window.addWidgetVlayout(display,True)
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    window.show()
    app.exec()