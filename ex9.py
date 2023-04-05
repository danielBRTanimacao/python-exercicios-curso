from os import system

lista_compras = [] #lista vazia

while True:
    opcao = str(input("Escolha uma opção\n[i]nserir [a]pagar [l]istar [s]air: ")).lower()[0]
    if opcao == 'i':
        system('cls')
        item = str(input("Valor: "))
        lista_compras.append(item) #adiciona o item a lista
    elif opcao == 'a':
        try:
            indice_del = int(input("Escolha um indice para apagar: "))
            lista_compras.pop(indice_del) #apaga o item escolhido
        except:
            print("Não foi possivel apagar!")
    elif opcao == 'l':
        system('cls')
        for i, c in enumerate(lista_compras): #[i] indice [c] contador
            print(i, c)
    if opcao == 's': #interrompe o programa
        break