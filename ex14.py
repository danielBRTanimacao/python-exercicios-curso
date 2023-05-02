def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    

duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
print(duplicar(2))