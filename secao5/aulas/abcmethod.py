from abc import ABC, abstractmethod
"""class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = name
        self._name = name
    @property
    @abstractmethod
    def name(self):...
    
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    

foo = Foo('bar')
print(foo.name)
 """
"""
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name
        self.name = name
               
    @property
    @abstractmethod
    def name(self): ...
    
class Foo(AbstractFoo):
    name = ''
    def __init__(self, name):
        super().__init__(name)

"""
class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name
        self.name = name
    @property
    def name(self):
        return self._name 
    @name.setter
    @abstractmethod
    def name(self, name):
        ...
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name
foo = Foo('teste')
print(foo.name)