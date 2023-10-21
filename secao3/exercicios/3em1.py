"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
""" try:
    num_int= int(input('informe um numero inteiro: '))
    if num_int%2 == 0:
        print('esse numero é divisivel por 2')
    else: 
        print('esse numero não é divisivel por 2')
except:
    print('O numero precisa ser inteiro, tente novamente.') """
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
""" try:
    hora = int(input('informe a hora do atual momento: '))
    if hora in range(0,12):
        print('Bom dia!!!')
    elif hora in range(12,18):
        print('Boa tarde!!!')
    elif hora in range(18,24):
        print('Boa noite!!!')
    else:
        print('Hora errada')
    
except:
    print('erro, tente novamente') """
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    nome = input('informe o seu primeiro nome: ')
    if len(nome) <= 4:
        print('Seu nome é curto') 
    elif len(nome) <= 6:
        print('Seu nome é normal')
    elif len(nome) < 6:
        print('Seu nome é muito grande')
except:
    print('Erro, tente novamente.')