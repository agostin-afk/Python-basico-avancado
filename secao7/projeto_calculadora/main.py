import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit,QPushButton
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import ICON_FILE
from display import Display
from infor import Infor
from tema import setupTheme
from buttons import Button


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    display = Display()
    botao1 = Button('botoa 1')
    icon = QIcon(str(ICON_FILE))
    info = Infor('teste')
    window.addWidgetVlayout(info, False)
    window.addWidgetVlayout(display,False)
    window.addWidgetVlayout(botao1, True)
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    window.show()
    app.exec()