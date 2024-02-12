from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variables import *
from utils import NumOrDot, isValidNumber, NumTransform
from typing import TYPE_CHECKING
from PySide6.QtCore import Slot
import math

if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
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
    def __init__(self, display: 'Display', info: 'Infor',window: 'MainWindow', *args, **kwargs) -> None:
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
        self.window = window
        self._makeGrid()
        
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
    def _makeGrid(self):
        
        self.display.eqPressed.connect(self._eq)
        
        self.display.clearPressed.connect(self._Clear)
        
        self.display.delPressed.connect(self.display.backspace)
        
        self.display.inputPressed.connect(self._insertTextToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)
        
        for i, row in enumerate(self._gridMask):
            for j, text in enumerate(row):
                if j == 1 and i == 4:
                    button = Button(text)
                    buttonText = button.text()
                    self.addWidget(button, i,j-1,1,2)
                    Slot = self._makeButtonDisplaySlot(self._insertTextToDisplay, buttonText)
                    self._connectButtonClicked(button, Slot)
                elif j == 0 and i==4:
                    pass
                else:
                    button = Button(text)
                    buttonText = button.text()
                    self.addWidget(button, i,j)
                    Slot = self._makeButtonDisplaySlot(self._insertTextToDisplay, buttonText)
                    self._connectButtonClicked(button, Slot)
                    
                if not NumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configEspecialButtons(button)
                

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
            self._makeButtonDisplaySlot(self._configLeftOp, text))
        if text == '=':
            self._connectButtonClicked(button, self._eq)
    @Slot()
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):

        def realSlot():
            func(*args, **kwargs)
        return realSlot
    @Slot()
    def _insertTextToDisplay(self, text: str):
        buttonText = text
        newDisplayValue = self.display.text() + buttonText
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)

    @Slot()
    def _eq(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return
        self._right = NumTransform(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        print(self.equation)
        print(self._left)
        result = 'Estouro'
        try:
            if '^' in self.equation and isinstance(self._left, (float, int)):
                print(result)
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
            result = NumTransform(result)
        except SyntaxError:
             self._Clear()
             self._showError("Conta incompleta")
        except ZeroDivisionError:
            self._showError(f"Erro de divisao por zero")
        except OverflowError as e:
            self._showError(f"Erro 45: {e}")
        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None
        if result == 'Estouro':
            self._left = None
        
    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()
       
        if  not isValidNumber(displayText):
            ...
            #self._showError('valor invalido')
        if self._left is None:
            if displayText == '':
                self._left = 0
            else:
                self._left = NumTransform(displayText)
        print(self.equation)
        self._op = text
        self.equation = f'{self._left} {self._op}'
        
        print(text)
        
    @Slot()
    def _Clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = ''
        self.display.clear()
    
    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox
    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()