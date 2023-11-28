import re
multiplicacao = 11
soma = 0
#cpf = input('informe seu cpf: ')
cpf = re.sub(r'[^0-9]', '', input('informe seu cpf: '))
#print(cpf)
entrada = cpf
teste_sequencia = entrada != cpf[0] * len(cpf)
if teste_sequencia:
    ...
    for i,k in enumerate(cpf[:11]):
        mult_valor = int(k) * multiplicacao
        soma += mult_valor
        multiplicacao -= 1
        if i == 9:
            penultimo_digito = int(k)
else:
    print('você digitou o mesmo numero em sequência, tente novamente!')



""" mult_numero = 10
for i,k in enumerate(cpf[:11]):
    
    if k in '.':
        pass
    else:
        mult_valor = int(k) * mult_numero
        soma += mult_valor
        mult_numero -= 1   
 """