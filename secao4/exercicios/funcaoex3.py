# Exercício - sistema de perguntas e respostas


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
    print("Opções:")
    for i, opcoes in enumerate(pergunta['Opções']):
        print(f'{i+1}) {opcoes}')
    print()
    escolha = input("Qual item está correto: ")
    acertou = False
    escolha_int = None
    if escolha.isdigit():
        escolha_int = int(escolha)
    if escolha_int is not None