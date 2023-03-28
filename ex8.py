def titulo(msg):
    print("-"*42)
    print(msg.center(42))
    print("-"*42)


#programa principal
titulo('Calculadora simples')
while True:
    numero1 = 0
    numero2 = 0
    operacoes = '/*-+'
    while True:
        try:
            numero1 = float(input("Digite um número: "))
            numero2 = float(input("Digite um segundo número: "))
            calculo = str(input("Qual operação deseja fazer! (/*+-) "))
            if calculo not in operacoes:
                print("Por favor um valor valido")
        except:
            print("Por favor digite um valor valido!")
        else:
            break
    #calculo
    if '-' in calculo:
        print(numero1-numero2)
    elif '/' in calculo:
        print(numero1/numero2)
    elif '+' in calculo:
        print(numero1+numero2)
    elif '*' in calculo:
        print(numero1*numero2)
    # Saida
    sair = input("Deseja sair? [s]sim, 'continuar e qualquer letra': ").lower().startswith('s')
    if sair:
        print("Obrigado por usar o programa!")
        break