import os
from itertools import count

caminho = os.path.join('C:\\Users','agost','OneDrive','Área de Trabalho')
contador = count()
for root, dirs, files in os.walk(caminho):
    o_contador = next(contador)
    print(o_contador, 'PASTA ATUAL: ', root)
    for dir_ in dirs:
        print(o_contador, 'DIRETORIO ATUAL: ', dir_)
    for file_ in files:
        print(o_contador, 'ARQUIVO ATUAL: ', file_)
