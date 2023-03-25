while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite algum operador (+-/*): ')
    num_val = None #numero valido recebe NONE

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

    #### Final ####

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
