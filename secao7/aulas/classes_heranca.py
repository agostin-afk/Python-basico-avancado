import sys 
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication, QGridLayout

app = QApplication(sys.argv)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.botao1 = QPushButton('botao 1')
        self.botao2 = QPushButton('botao 2')
        self.botao1.setStyleSheet('font-size: 12px; font-weight: bold; color: red')
        self.botao2.setStyleSheet('font-size: 12px; font-weight: bold; color: green') 
        self.central_widget = QWidget()
        self.layout_grid = QGridLayout()

        self.layout_grid.addWidget(self.botao1)
        self.layout_grid.addWidget(self.botao2)


        self.central_widget.setLayout(self.layout_grid)

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('minha janela')

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('minha primeira mensagem')
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('primeiro menu')
        
        self.primeira_acao = self.primeiro_menu.addAction('primeira acao')
        self.primeira_acao.triggered.connect(self.slot_segunda_mensagem)
        self.segunda_acao = self.primeiro_menu.addAction('segunda acao')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.check)
        self.segunda_acao.hovered.connect(self.check)
        self.botao1.clicked.connect(self.check)

    @Slot()
    def slot_segunda_mensagem(self):
        self.status_bar.showMessage('minha segunda mensagem')
    
    @Slot()    
    def check(self):
        print('esta marcado ?:',self.segunda_acao.isChecked())
        


window = MyWindow()

window.show()

app.exec()