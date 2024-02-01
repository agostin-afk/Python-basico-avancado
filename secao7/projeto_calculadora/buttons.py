from PySide6.QtWidgets import QPushButton
from variables import *
from tema import qss

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    def configStyle(self):
        font = self.font()
        font.setPixelSize(SMALL_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(65,65)
        self.setProperty('cssClass', 'specialButton')