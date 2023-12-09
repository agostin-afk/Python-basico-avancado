""" x = 1
def escopo():
    x = 10
    y = 2
    def func_interna():
        y= 20
        print(f'valor de x= {x}\nvalor de y= {y}\nNa função "func_interna"\n')      
    func_interna()
    
    print(f'valor de x= {x}\nvalor de y= {y}\nNa função "escopo"\n')
print(f'valor de x= {x} fora das funções')
escopo()
print(f'valor de x= {x} fora das funções') """

x = 1
def escopo():
    global x
    x = 10
    y = 2
    def func_interna():
        y= 20
        print(f'valor de x= {x}\nvalor de y= {y}\nNa função "func_interna"\n')      
    func_interna()
    
    print(f'valor de x= {x}\nvalor de y= {y}\nNa função "escopo"\n')
print(f'valor de x= {x} fora das funções')
escopo()
print(f'valor de x= {x} fora das funções')