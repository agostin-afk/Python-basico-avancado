class Caneta:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor_tinta = cor
    @property
    def cor(self):
        return self.cor_tinta
    @cor.setter
    def cor(self, valor):
        self.cor_tinta = valor
        
caneta1 = Caneta('Bic', 'azul')
caneta1.cor = 'vermelho'
print(caneta1.cor)