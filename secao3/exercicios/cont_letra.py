string = 'isso eh um teste para contador de letras feito pelo agostinho ferreira'

i = 0
qtd_letra_mais = 0
letra_mais = ' '
while i < len(string):
    letra_atual = string[i]
    if letra_atual == ' ':
        i += 1
        continue
    qtd_atual = string.count(letra_atual)
    if qtd_letra_mais < qtd_atual:
        qtd_letra_mais = qtd_atual
        letra_mais = letra_atual
    i+=1
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais}" que apareceu '
    f'{qtd_letra_mais}x'
)