string = "Agostinho Ferreira"

i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
else:
    print("O while foi executado até o final e esse é o else!")
i = 0
#o codigo abaixo, o else não é exexutado pois existe um break que interrompe o while, e por consequencia o else
while i < len(string):
    letra = string[i]
    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print("O while foi executado até o final e esse é o else!")
