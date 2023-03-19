valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
if valor1 > valor2: #ou >= eliminando o elif
    print(f"O maior valor e o valor 1 '{valor1}'")
elif valor1 == valor2:
    print("Os dois valores são iguais")
else:
    print(f"O maior valor e o valor 2 '{valor2}'")