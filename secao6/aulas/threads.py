from time import sleep
from threading import Thread

class MyThread(Thread):
    def __init__(self, texto, tempo):
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