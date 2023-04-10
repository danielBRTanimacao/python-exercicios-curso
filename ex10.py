cpf = '588.510.240-65'
format_pontos = cpf.replace('.', '').replace('-', '') #CPF FORMATADO
limit_digitos = format_pontos[:9] #LIMITA LEITURA CPF
num_multiplicar = 10 #Número multiplicar

resultado = 0 #Resultado das somas

for contador in limit_digitos:
    print(f'{contador} X {num_multiplicar} = {int(contador) * num_multiplicar}')
    resultado += int(contador) * num_multiplicar
    num_multiplicar += -1

print(f"A soma e {resultado}")
resultado = (resultado * 10) % 11 #soma final
if resultado > 9:
    print("O resultado final e ZERO")
else:
    print(f"O resultado final e {resultado}")