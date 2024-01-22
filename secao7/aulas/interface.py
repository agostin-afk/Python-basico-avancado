import sys
from PySide6.QtWidgets import QApplication,QPushButton

app = QApplication(sys.argv)
botao = QPushButton('texto do botao')
botao.setStyleSheet('font-size: 30px; color: red')
botao.show()

app.exec()