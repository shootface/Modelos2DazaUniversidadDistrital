def potencia(base,exponente):
    if exponente==0:
        return 1
    elif exponente%2==0:
        return potencia(base*base,exponente/2)
    else:
        return base*potencia(base,exponente-1)

print(potencia(2,2))