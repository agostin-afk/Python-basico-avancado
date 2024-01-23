import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication,QWidget,QGridLayout


app = QApplication(sys.argv)

botao1 = QPushButton('Botão 1')
botao2 = QPushButton('Botão 2')
botao1.setStyleSheet('font-size: 12px; font-weight: bold; color: red')
botao2.setStyleSheet('font-size: 12px; font-weight: bold; color: green')

window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()


layout.addWidget(botao1)
layout.addWidget(botao2)


central_widget.setLayout(layout)


window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela')


status_bar = window.statusBar()
status_bar.showMessage('Mensagem')
def slot_exemple(sb):
    sb.showMessage('Mensagem nova')

menu = window.menuBar()
primeiro_menu = menu.addMenu('primeiro menu')


primeira_acao = primeiro_menu.addAction('primeira acao')
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar))


window.show()

app.exec()