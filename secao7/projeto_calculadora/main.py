import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit,QPushButton
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import ICON_FILE
from display import Display
from infor import Infor
from tema import setupTheme
from buttons import Button, ButtonsGrid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    
    
    info = Infor('teste')
    window.addWidgetVlayout(info, False)
    
    
    display = Display()
    window.addWidgetVlayout(display,False)
    
    
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)
    window.adjustFixedSize()
    
    
    
    icon = QIcon(str(ICON_FILE))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    
    
    window.show()
    app.exec()