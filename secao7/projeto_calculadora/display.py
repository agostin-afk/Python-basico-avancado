from PySide6.QtWidgets import QLineEdit
from variables import *
from  PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px')
        self.setMinimumHeight(SMALL_FONT_SIZE*2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN_DEFAULT for _ in range(4)])