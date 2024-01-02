
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
     property
    @motor.setter
    def motor(self, value):
        self._motor = value
        
    @property
class Motor:
    
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    
    def __init__(self, nome):
        self.nome = nome
        
carro1 = Carro('gol')
motor1 = Motor('v8')
carro1.motor = motor1

print(carro1.motor)