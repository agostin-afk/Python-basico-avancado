def mult(*args):
    multiplicacao = 1
    for _ in args:
        multiplicacao *= _
    return multiplicacao
multiplicacao = mult(2)
print(multiplicacao)
def imparpar(valor):
    teste = valor % 2 == 0
    if teste:
        return f"{valor} é par"
    else:
        return f"{valor} é ímpar"
print(imparpar(multiplicacao))