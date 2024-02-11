from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import *
from  PySide6.QtCore import Qt, Signal
from utils import isEmpty

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px')
        self.setMinimumHeight(SMALL_FONT_SIZE*2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN_DEFAULT for _ in range(4)])
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Delete, KEYS.Key_Backspace]
        isEsc = key in [KEYS.Key_Escape]
        
        if isEnter or text == '=':
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            self.delPressed.emit()
            return event.ignore()
        
        if isEsc:
            self.clearPressed.emit()
            return event.ignore()
        if isEmpty(text):
            return event.ignore()