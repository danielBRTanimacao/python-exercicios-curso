def multiplicar(*args): #args argumentos
    total = 1
    for numeros in args:
        total *= numeros
    return total
    

multi = multiplicar(1, 2, 3, 4, 5)
print(multi)