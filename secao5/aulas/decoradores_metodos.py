def meu_repr(self):
    class_name = type(self).__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} => {class_dict}'
    return class_repr

def add_repr(cls):
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'Terra' in resultado:
            return 'Você está em casa!'
        return resultado
    return interno


@add_repr
class Time:
    def __init__(self, name):
        self.name = name
@add_repr     
class Planeta:
    def __init__(self, name):
         self.name = name
         
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.name}'


terra = Planeta('Terra')
marte = Planeta('Marte')
brasil = Time('Brasil')
argentina = Time('Argentina')

print(terra)
print(marte)
print(brasil)
print(argentina)

print(terra.falar_nome())
print(marte.falar_nome())