class Camera:
    def __init__(self, nome, filmando= False):
        self.nome = nome
        self.filmando = filmando
    def filmar(self):
        if self.filmando:
            print('A camera já está filmando.')
            return
        print(f'{self.nome} está filmando')
        self.filmando = True
    def parar_filmar(self):
        if not self.filmando:
            print(f'A camera {self.nome} não está filmando')
            return
        print(f'{self.nome} parou de filmar')
        self.filmando = False
    


c1 = Camera('Canon')
print(c1.nome)
c1.filmar()
c1.filmar()
c1.parar_filmar()
c1.parar_filmar()