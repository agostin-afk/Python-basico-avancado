
while True:
    num1 = input('informe um numero: ')
    num2 = input('informe outro numero: ')
    operadores_escolha = input('informe uma operação[+, -, *, =, /]: ')
    teste_numero = None
    num1_convert = 0
    num2_convert = 0
    try: 
        num1_convert = float(num1)
        num2_convert = float(num2)
        teste_numero = True
    except:
        teste_numero = None
        
    if not teste_numero:
        print("Um ou ambos os numeros foram digitados incorretamente, tente novamente!!!")
        continue
    operadores = '+-/*/'
    if operadores_escolha not in operadores:
        print('operador inválido, tente novamente!')
    if len(operadores_escolha) > 1:
        print('Digite apenas um operador, tente novamente!')
    print('Realizando a sua conta, confira o valor abaixo:')
    if operadores_escolha == '+':
        print(f'{num1_convert} + {num2_convert} = {num1_convert+num2_convert}')
    elif operadores_escolha == '-':
        print(f'{num1_convert} - {num2_convert} = {num1_convert-num2_convert}')
    elif operadores_escolha == '*':
        print(f'{num1_convert} * {num2_convert} = {num1_convert*num2_convert}')
    elif operadores_escolha == '/':
        print(f'{num1_convert} / {num2_convert} = {num1_convert/num2_convert}')
    sair = input('voce deseja sair ? Sim para sair: ').lower().startswith('s')
    if sair: 
        break