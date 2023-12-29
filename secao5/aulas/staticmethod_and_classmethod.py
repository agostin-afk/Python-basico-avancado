class Conection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_name(self, name):
        self.user = name
    
    def set_password(self, password):
        self.password = password
        
    @classmethod
    def create_with_auth(cls, user, password):
        conection = cls()
        conection.user = user
        conection.password = password
        return conection
    
    @staticmethod
    def mensagem():
        print('login realizado')
        
c1 = Conection.create_with_auth("lucas", 123456)
c2 = Conection()
c2.set_name('pedro')
c2.set_password(123456)
c3 = Conection()
lista = [c1, c2, c3]
for _ in lista:
    print(vars(_), sep='\n')
    if _.user is not None:
        Conection.mensagem()