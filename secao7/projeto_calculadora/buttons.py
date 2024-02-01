from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import *
from utils import NumOrDot



class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    def configStyle(self):
        font = self.font()
        font.setPixelSize(SMALL_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(65,65)
        
        
class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._makeGrid()
    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, text in enumerate(row):
                if j == 1 and i == 4:
                    button = Button(text)
                    self.addWidget(button, i,j-1,1,2)
                elif j == 0 and i==4:
                    pass
                else:
                    button = Button(text)
                    self.addWidget(button, i,j)
                if not NumOrDot(text):
                    button.setProperty('cssClass', 'specialButton')
