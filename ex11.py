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

dez_digitos = limit_digitos + str(resultado)
contador_regressivo_2 = 11

resultado_digito_2 = 0 #Esta com BUG
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{limit_digitos}{resultado}{digito_2}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')