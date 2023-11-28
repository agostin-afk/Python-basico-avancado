soma = 0
cpf = '111.111.111-00'
mult_numero = 10
for i,k in enumerate(cpf[:11]):
    
    if k in '.':
        pass
    else:
        mult_valor = int(k) * mult_numero
        soma += mult_valor
        mult_numero -= 1   
validcao = cpf[12]
teste_soma = soma*10
teste_resto = teste_soma%11
if teste_resto > 9:
    resultado = 0
else:
    resultado = teste_resto    
if resultado == int(cpf[12]):
    print('seu cpf é valido!!')
else:
    print('seu cpf não é valido!!!')