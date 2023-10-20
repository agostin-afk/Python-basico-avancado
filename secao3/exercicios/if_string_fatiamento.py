"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('informe seu nome: ')
idade = int(input('informe a sua idade: '))
if (nome and idade):
    print(f'Seu nome é {nome}\n'
          f'Seu nome invertido fica {nome[::-1]}\n'
          f'Seu nome {"" if "" in nome else "não"} contém espaços\n'
          f'Seu nome tem {len(nome)} letras\n'
          f'A primeira letra do seu nome é: {nome[0]}\n'
          f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")