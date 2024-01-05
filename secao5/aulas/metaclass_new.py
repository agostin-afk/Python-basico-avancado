class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('MEU META NEW')
        cls = super().__new__(mcs, name, bases, dct)
        return cls
class Pessoa:
    def __new__(cls):
        print('MEU NEW')
        instance  = super().__new__(cls)
        return instance
    def __init__(self,name):
        print('MEU INIT')
        self.name = name 

p1 = Pessoa('Agosto')