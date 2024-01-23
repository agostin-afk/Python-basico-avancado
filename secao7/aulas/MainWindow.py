import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication,QWidget,QGridLayout


app = QApplication(sys.argv)

botao1 = QPushButton('Botão 1')
botao2 = QPushButton('Botão 2')
botao1.setStyleSheet('font-size: 12px; font-weight: bold; color: red')
botao2.setStyleSheet('font-size: 12px; font-weight: bold; color: green')

central_widget = QWidget()
layout = QGridLayout()
layout.addWidget(botao1)
layout.addWidget(botao2)
central_widget.setLayout(layout)

central_widget.show()




app.exec()