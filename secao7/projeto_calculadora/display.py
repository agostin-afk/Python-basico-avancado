from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import *
from  PySide6.QtCore import Qt, Signal

class Display(QLineEdit):
    eqRequested = Signal()
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
        key = event.key()
        KEYS = Qt.Key
        
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        if isEnter:
            self.eqRequested.emit()
            return event.ignore()