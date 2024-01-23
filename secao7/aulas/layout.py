import sys 
from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QGridLayout

app = QApplication(sys.argv)
botao1 = QPushButton('teste do botão')
botao2 = QPushButton('teste botão 2')
botao1.setStyleSheet('font-size: 12px; font-weight: bold; color: red')
botao2.setStyleSheet('font-size: 12px; font-weight: bold; color: green')

central_widget = QWidget()
layout = QGridLayout()
layout.addWidget(botao1, 1, 1)
layout.addWidget(botao2, 1, 2)
central_widget.setLayout(layout)
central_widget.show()

app.exec()