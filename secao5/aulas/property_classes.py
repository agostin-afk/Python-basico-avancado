class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        
    @property
    def cor(self):
        return self.cor_tinta
    
caneta = Caneta('vermelho')
print(f'A cor da caneta é: {caneta.cor}')