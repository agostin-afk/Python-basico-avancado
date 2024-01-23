import sys
from PySide6.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication, QGridLayout

app = QApplication(sys.argv)

botao1 = QPushButton('botoa 1')
botao2 = QPushButton('botao 2')
botao1.setStyleSheet('font-size: 12px; font-weight: bold; color: red')
botao2.setStyleSheet('font-size: 12px; font-weight: bold; color: green')


window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()

layout.addWidget(botao1)
layout.addWidget(botao2)


central_widget.setLayout(layout)


window.setCentralWidget(central_widget)

window.setWindowTitle('minha janela')

status_bar = window.statusBar()
status_bar.showMessage('minha primeira mensagem')


def slot_exemple(sb):
    sb.showMessage('minha segunda mensagem')

def outro_slot(checked):
    print('esta marcado? ', checked)

def mais_um_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


menu = window.menuBar()
primeiro_menu = menu.addMenu('primeiro menu')

primeira_acao = primeiro_menu.addAction('primeira acao')
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar))

segunda_acao = primeiro_menu.addAction('segunda acao')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(mais_um_slot(segunda_acao))

botao1.clicked.connect(mais_um_slot(segunda_acao))

window.show()

app.exec()
