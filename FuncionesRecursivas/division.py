def division(a,b):
    if a<b:
        return 0
    else:
        return 1+division(a-b,b)

print(division(15,3))