def sumadigitos(n):
    if n==0:
        return 0
    else:
        return n%10+sumadigitos(n/10)

print(sumadigitos(123))