from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import *
from utils import NumOrDot, isValidNumber
from display import Display



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
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()
    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, text in enumerate(row):
                if j == 1 and i == 4:
                    buttonText = Button(text)
                    self.addWidget(buttonText, i,j-1,1,2)
                    buttonSlot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplat, buttonText)
                    buttonText.clicked.connect(buttonSlot)  
                elif j == 0 and i==4:
                    pass
                else:
                    buttonText = Button(text)
                    self.addWidget(buttonText, i,j)
                    buttonSlot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplat, buttonText)
                    buttonText.clicked.connect(buttonSlot)  
                if not NumOrDot(text):
                    buttonText.setProperty('cssClass', 'specialButton')
                

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    def _insertButtonTextToDisplat(self,button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)