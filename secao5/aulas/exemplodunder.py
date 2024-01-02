class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        #class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r})'
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        
        return Ponto(novo_x, novo_y)
if __name__ == '__main__':
    p1 = Ponto(4,2)
    p2 = Ponto(6,4)
    p3 = p1+p2
    print(p3)