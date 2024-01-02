
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, value):
        self._motor = value
        
    @property
    def faricante(self):
        return self._fabricante
    @faricante.setter
    def fabricante(self, value):
        self._fabricante = value
class Motor:
    
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    
    def __init__(self, nome):
        self.nome = nome
        
carro1 = Carro('gol')
motor1 = Motor('1.0')
fabricante1 = Fabricante('Volkswagen')
carro1.fabricante = fabricante1
carro1.motor = motor1

print(vars(carro1), sep='\n')
print(f'{carro1.nome}\n{carro1.fabricante.nome}\n{carro1.motor.nome}')