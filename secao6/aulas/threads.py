from time import sleep
from threading import Lock, Thread
'''
class MyThread(Thread):
    def __init__(self, texto: str, tempo: int):
        self.texto = texto
        self.tempo = tempo
        super().__init__()
    def run(self):
        sleep(self.tempo)
        print(self.texto)
        
t1 = MyThread('agosto', 5)
t2 = MyThread('é',7)
t3 = MyThread('legal', 9)

t1.start()
t2.start()
t3.start()

for _ in range(10):
    print(_)
    sleep(1)
    
''' 

'''
def contador(texto: str, tempo: int):
    sleep(tempo)
    print(texto)

th1 = Thread(target=contador, args=('ola, contei já', 10))
th1.start()

while th1.is_alive():
    print('a thread não acabou')
    sleep(2) 
'''

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()
        
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('não temos ingresso(os) suficientes')
            self.lock.release()
            return
        
        self.estoque -= quantidade
        
        print(f'voce comprou {quantidade} ingresso(os) ainda temos no estoque: {self.estoque}')
        self.lock.release()
ingresso = Ingressos(10)
for i in range(1,10):
    t = Thread(target= ingresso.comprar, args= (i,))
    t.start()