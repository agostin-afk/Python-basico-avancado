import json
from salvando_dados_classes import CAMINHO_ARQUIVO, Pessoa, salvando

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    print(*dados, sep='\n')