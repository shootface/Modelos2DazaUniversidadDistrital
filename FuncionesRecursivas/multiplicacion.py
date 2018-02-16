def multiplicacion(a,b):
    if b==0:
        return 0
    else:
        return a+multiplicacion(a,b-1)

print(multiplicacion(5.2,3))