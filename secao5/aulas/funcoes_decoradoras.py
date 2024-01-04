
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} ({class_dict})'
    return class_repr

def add_class(cls):
    cls.__repr__ = meu_repr
    return cls
    
    
""" class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr
         """
@add_class
class Time:
    def __init__(self, nome):
        self.nome = nome



@add_class
class Planeta:
    def __init__(self, nome):
        self.nome = nome
        
brasil = Time('BRASIL')
portugal = Time('PORTUGAL')
marte = Planeta('Marte')
terra = Planeta('Terra')



print(brasil)
print(terra)