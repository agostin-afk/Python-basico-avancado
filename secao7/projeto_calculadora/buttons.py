from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import *
from utils import NumOrDot, isValidNumber, NumTransform
from typing import TYPE_CHECKING
from PySide6.QtCore import Slot
import math

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
            
        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)
            
        if text in '+-*/^':
            self._connectButtonClicked(button, 
            self._makeButtonDisplaySlot(self._OperatorClicked,button))
        
        if text in '=':
            self._connectButtonClicked(button, self._eq)
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
    
    def _eq(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return
        self._right = NumTransform(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        print(self.equation)
        result = 'Estouro'
        try:
            if '^' in self.equation and isinstance(self._left, (float, int)):
                print(result)
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
            result = NumTransform(result)
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
        except OverflowError as e:
            print(f"Erro 45: {e}")
        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None
        if result == 'Estouro':
            self._left = None
        
    def _OperatorClicked(self, button):
        text = button.text()
        displayText = self.display.text()
        self.display.clear()
       
        if  not isValidNumber(displayText) and self._left is None:
            print('nada no valor da esquerda')
        
        if self._left is None:
            self._left = NumTransform(displayText)
        self._op = text
        self.equation = f'{self._left} {self._op}'
        
        print(text)
    def _Clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = ''
        self.display.clear()