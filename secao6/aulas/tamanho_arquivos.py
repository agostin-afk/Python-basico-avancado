import os
from itertools import count
import math

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    if tamanho_em_bytes <= 0:
        return "0B"
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = os.path.join('C:\\Users','agost','OneDrive','Área de Trabalho')
contador = count()
for root, dirs, files in os.walk(caminho):
    o_contador = next(contador)
    print(o_contador, 'PASTA ATUAL: ', root)
    for dir_ in dirs:
        print(o_contador, 'DIRETORIO ATUAL: ', dir_)
    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_completo)
        print(o_contador, 'ARQUIVO ATUAL: ', file_, formata_tamanho(tamanho))
