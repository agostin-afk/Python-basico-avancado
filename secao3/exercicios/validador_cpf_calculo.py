import re
multiplicacao = 10
soma = 0
#cpf = input('informe seu cpf: ')
cpf = re.sub(r'[^0-9]', '', input('informe seu cpf: '))
entrada = cpf
teste_sequencia = entrada != cpf[0] * len(cpf)
if teste_sequencia:
    ...
    for i,k in enumerate(cpf[:11]):
        mult_valor = int(k) * multiplicacao
        soma += mult_valor
        multiplicacao -= 1
        if i == 9:
            penultimo_digito = k
            soma_digi_1 = soma * 10
            soma_digi_1 %= 11
            resultado_digi_1 = soma_digi_1 if soma_digi_1 <= 9 else 0
        if i == 10:
            ultimo_digito = k
            soma_digi_2 = soma * 10
            soma_digi_2 %= 11
            resultado_digi_2 = soma_digi_2 if soma_digi_2 <= 9 else 0
        #print(resultado_digi_1)
    print(resultado_digi_1)
        
    # print(cpf[9:])
    
    
else:
    print('você digitou o mesmo numero em sequência, tente novamente!')
