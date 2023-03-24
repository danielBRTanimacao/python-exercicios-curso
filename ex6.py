nome = input("Digite algo: ")
tamanho_nome = len(nome)
fim = 0
novo_nome = ''
while fim < tamanho_nome:
    fim += 1
    novo_nome += '*' + nome[fim-1]
    if fim == tamanho_nome:
        print(novo_nome)
        break
