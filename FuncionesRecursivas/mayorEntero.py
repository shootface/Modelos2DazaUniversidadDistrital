def mayor(n,c):
    if int(n)!=0:
        if c<int((abs(n) - abs(int(n)))*10):
            return mayor(n/10,int((abs(n) - abs(int(n)))*10))
        else:
            return mayor(n/10,c)
    elif int((abs(n) - abs(int(n)))*10)!=0:
        if c<int((abs(n) - abs(int(n)))*10):
            return mayor(n/10,int((abs(n) - abs(int(n)))*10))
        else:
            return mayor(n/10,c)
    else:
        return c
        
print(mayor(34343254365,0))