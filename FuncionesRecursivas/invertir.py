def invertir(a,b):
    if int(a)!=0:
        return invertir(a/10,b+str(int(round((abs(a) - abs(int(a)))*10,0))))
    elif int((abs(a) - abs(int(a)))*10)!=0:
        return invertir(a/10,b+str(int((abs(a) - abs(int(a)))*10)))
    else:
        return int(b)