import re
multiplicacao_1 = 10
multiplicacao_2 = 11
cal_num1 = cal_num2 =0


cpf = re.sub(r'[^0-9]', '', input('informe seu cpf: '))
teste_sequencia = cpf != cpf[0] * len(cpf)
if teste_sequencia:
    for i,k in enumerate(cpf):
        mult_valor_1 = int(k) * multiplicacao_1
        mult_valor_2 = int(k) * multiplicacao_2
        cal_num1 += mult_valor_1
        cal_num2 += mult_valor_2
        multiplicacao_1 -= 1
        multiplicacao_2 -= 1
        if i == 8:
            penultimo_digito = cpf[i+1]
            cal_num1 *= 10
            cal_num1 %= 11
            resultado_digi_1 = cal_num1 if cal_num1 <= 9 else 0
        if i == 9:
            ultimo_digito = cpf[i+1]
            cal_num2 *= 10
            cal_num2 %= 11
            resultado_digi_2 = cal_num2 if cal_num2 <= 9 else 0
    if resultado_digi_2 == int(ultimo_digito) and resultado_digi_1 == int(penultimo_digito):
        print('cpf valido!')   
    else:
        print('cpf invalido!')
else:
    print('você digitou o mesmo numero em sequência, tente novamente!')
