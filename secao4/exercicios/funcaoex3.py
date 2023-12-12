# Exercício - sistema de perguntas e respostas


import os


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    alternativas = pergunta['Opções']
    print("Opções:")
    
    for index, opcao in enumerate(alternativas):
        print(f'{index}) {opcao}')
    
    print()
    
    escolha = input("Qual item está correto: ")
    acertou = False
    escolha_int = None
    qtd_acertos = 0
    qtd_opcoes = len(alternativas)
    if escolha.isdigit():
        escolha_int = int(escolha)
    if escolha_int is not None:
        
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            
            if alternativas[escolha_int] == pergunta['Resposta']:
                qtd_acertos += 1
                acertou = True
    os.system('cls')
    if acertou:
        print(f"Você acertou! Resposta: {pergunta['Resposta']}")
    else:
        print(f"Você errou! Resposta: {pergunta['Resposta']}")
print(f'você acertou {qtd_acertos} de {len(pergunta)} perguntas!')