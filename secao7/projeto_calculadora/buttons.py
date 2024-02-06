from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import *
from utils import NumOrDot, isValidNumber
from typing import TYPE_CHECKING
from PySide6.QtCore import Slot


if TYPE_CHECKING:
    from display import Display
    from infor import Infor



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
    def __init__(self, display: 'Display', info: 'Infor', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self._makeGrid()
        
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, text in enumerate(row):
                if j == 1 and i == 4:
                    buttonText = Button(text)
                    self.addWidget(buttonText, i,j-1,1,2)
                    Slot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplat, buttonText)
                    self._connectButtonClicked(buttonText, Slot)
                elif j == 0 and i==4:
                    pass
                else:
                    buttonText = Button(text)
                    self.addWidget(buttonText, i,j)
                    Slot = self._makeButtonDisplaySlot(self._insertButtonTextToDisplat, buttonText)
                    self._connectButtonClicked(buttonText, Slot)
                    
                if not NumOrDot(text):
                    buttonText.setProperty('cssClass', 'specialButton')
                    self._configEspecialButtons(buttonText)
                

    def _connectButtonClicked(self, button, Slot):
        button.clicked.connect(Slot)
    
    def _configEspecialButtons(self, button):
        text = button.text()
        
        if text == 'C':
            self._connectButtonClicked(button, self._Clear)
        if text in '+-*/':
            self._connectButtonClicked(button, 
            self._makeButtonDisplaySlot(self._OperatorClicked,button))
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
    def _OperatorClicked(self, button):
        text = button.text()
        displayText = self.display.text()
        self.display.clear()
       
        if  not isValidNumber(displayText) and self._left is None:
            print('nada no valor da esquerda')
        
        if self._left is None:
            self._left = float(displayText)
        self._op = text
        self.equation = f'{self._left} {self._op}'
        
        print(text)
    def _Clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = ''
        self.display.clear()