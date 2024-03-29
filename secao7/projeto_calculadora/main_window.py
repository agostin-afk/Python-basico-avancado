from PySide6.QtWidgets import QMessageBox, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.cw = QWidget()
        self.setCentralWidget(self.cw)
        self.vLayout = QVBoxLayout(self.cw)
        self.setLayout(self.vLayout)
        self.setWindowTitle('Calculadora do Agosto')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetVlayout(self, widget: QWidget, autoajuste: bool = True):
        self.vLayout.addWidget(widget)
        if autoajuste:
            self.adjustFixedSize()

    def makeMsgBox(self):
        return QMessageBox(self)
