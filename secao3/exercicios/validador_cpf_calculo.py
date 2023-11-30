import re
'''
0  8  9 7 8 0 0 7 3 7 6
11 10 9 8 7 6 5 4 3 2 1
 
'''
multiplicacao_1 = 10
multiplicacao_2 = 11
soma_1 = 0
soma_2 = 0
#cpf = input('informe seu cpf: ')
cpf = re.sub(r'[^0-9]', '', input('informe seu cpf: '))
entrada = cpf
teste_sequencia = entrada != cpf[0] * len(cpf)
if teste_sequencia:
    ...
    for i,k in enumerate(cpf):
        mult_valor_1 = int(k) * multiplicacao_1
        mult_valor_2 = int(k) * multiplicacao_2
        soma_1 += mult_valor_1
        soma_2 += mult_valor_2
        multiplicacao_1 -= 1
        multiplicacao_2 -= 1
        if i == 8:
            penultimo_digito = k
            soma_digi_1 = soma_1 * 10
            soma_digi_1 = soma_digi_1%11
            resultado_digi_1 = soma_digi_1 if soma_digi_1 <= 9 else 0
        if i == 9:
            ultimo_digito = k
            soma_digi_2 = soma_2 * 10
            soma_digi_2 %= 11
            resultado_digi_2 = soma_digi_2 if soma_digi_2 <= 9 else 0
        
    # print(cpf[9:])
    
    
else:
    print('você digitou o mesmo numero em sequência, tente novamente!')
