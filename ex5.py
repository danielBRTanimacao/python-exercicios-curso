"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
try:
    numero = int(input("Digite um número inteiro: "))
except:
    print("Digite um número inteiro valido! ex '1, 2, 3..'")
else:
    if numero % 2 == 0:
        print("\033[32mSim\033[m, esse número e \033[32mPAR\033[m!")
    else:
        print("\033[31mNão\033[m, esse número é \033[31mIMPAR\033[m... e não par")

"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
hora = float(input("Digite as horas: "))
if hora == 0 or hora <= 11:
    print("Bom dia!")
elif hora == 12 or hora <= 17:
    print("Boa tarde!")
elif hora == 18 or 23:
    print("Boa noite!")
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""