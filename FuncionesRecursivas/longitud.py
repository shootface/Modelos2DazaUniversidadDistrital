def lon(a,b):
    if int(a)!=0:
        return lon(a/10,b+1)
    else:
        return b

print(lon(12345891234,0))