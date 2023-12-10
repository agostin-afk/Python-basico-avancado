def soma(a,b,c=None):
    if c is not None:
        print(f"a= {a}, b= {b}, c= {c}\nA soma é: {a+b+c}")
    else:
        print(f"a= {a}, b= {b}\nA soma é: {a+b}")
soma(1,2)
soma(5,0,9)