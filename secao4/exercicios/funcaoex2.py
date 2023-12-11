def criar_mult(multiplicador):
    def multiplicar(num):
        num *= multiplicador
        return num
    return multiplicar
duplicar = criar_mult(2)
triplicar = criar_mult(3)
quadricar = criar_mult(4)
print(duplicar(3))
print(triplicar(3))
print(quadricar(3))