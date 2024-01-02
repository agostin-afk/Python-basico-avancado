class Eletronico:
    def __init__(self, nome):
        self._nome = nome 
        self._ligado = False
    def ligar(self):
        if not self._ligado:
            self._ligado = True
    def desligar(self):
        if self._ligado:
            self._ligado = False
            
class Smartphone(Eletronico):
    ...