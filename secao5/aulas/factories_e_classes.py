class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Sem nome', idade)
    @classmethod
    def criar_idade_45(cls, nome):
        return cls(nome, 45)
    
p1 = Pessoa('Mateus', 18)
p2 = Pessoa.criar_sem_nome(20)
p3 = Pessoa.criar_idade_45('lúcia')
lista = [p1, p2, p3]

for _ in lista:
    print(f'{_.nome}: {_.idade} anos', sep='\n')