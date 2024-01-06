import json
CAMINHO_ARQUIVO = 'secao5\\exercicios\\salvando_dados_classes.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('pedro', 18)
p2 = Pessoa('lucas', 19)
p3 = Pessoa('Maria', 20)
db = [vars(p1), vars(p2), vars(p3)]
def salvando():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(db, arquivo,indent=2,ensure_ascii=False)
if __name__ == '__main__':
    salvando()