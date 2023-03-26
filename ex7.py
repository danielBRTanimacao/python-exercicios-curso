while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite algum operador (+-/*): ')
    num_val = None #numero valido recebe NONE

    num_1f = 0 
    num_2f = 0
    try:
        num_1f = float(num_1)   #Tenta transformar os números
        num_2f = float(num_2)   #
        num_val = True       #Valida o num
    except:
        num_val = None 

    if num_val is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*' #validar operadores
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    #### Calculos ####
    if operador == '+':
        print(f"{num_1} + {num_2} = {num_1f+num_2f}")
    elif operador == '*':
        print(f"{num_1} x {num_2} = {num_1f*num_2f}")
    elif operador == '':
        print(f"{num_1} / {num_2} = {num_1f/num_2f}")
    elif operador == '':
        print(f"{num_1} - {num_2} = {num_1f-num_2f}")
    else:
        print("Você não deveria chegar aqui!")
    #### Final ####

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
