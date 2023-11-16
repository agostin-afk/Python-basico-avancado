"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de
índices inexistentes na lista.

"""
import os


lista = []
escolha = ''
while True:
    try: 
        escolha = input('informe uma operação:\n[a] para apagar\n[i] inserir\n[l] para listar\nEscolha sua escolha: ').lower().split()[0]
        if escolha == 'a':
            os.system('cls')
            indice = int(input('escolha o indice: ')) -1
            lista.pop(indice)
        elif escolha == 'i':
            os.system('cls')
            valor = input('informe oque deseja inserir: ')
            lista.append(valor)
        elif escolha == 'l':
            for i,k in enumerate(lista):
                print(f'{i+1} {k}')
        elif escolha == 0:
            break
    except IndexError:
        print('Operação inválida, erro de indice, tente novamente!!')
    except KeyboardInterrupt:
        print('sistema interrompido pelo usuario!')
        break