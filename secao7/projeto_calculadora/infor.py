from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import MIDIUM_FONT_SIZE


class Infor(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {MIDIUM_FONT_SIZE}')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
