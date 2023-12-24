# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
"""def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    nova_lista = [
        (lista1[_], lista2[_]) for _ in range(intervalo_maximo)
    ]
    return nova_lista
print(zipper(l1,l2)) """

from itertools import zip_longest

print(list(zip(l1,l2)))

print()

print(list(zip_longest(l1,l2, fillvalue='Sem cidade')))