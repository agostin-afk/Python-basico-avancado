class Pessoa:
    ano_atual = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
pessoa1 = Pessoa('pedro', 20)

print(pessoa1.get_ano_nascimento())