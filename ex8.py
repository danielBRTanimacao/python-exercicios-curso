from os import system

print("-"*42)
print("Jogo da palavra secreta!".center(42)) #titulo game
print("-"*42)
palavra = 'batata' #palavra secreta
# palavra = str(input('digite alguma palavra para alguem adivinhar: ')) #sem try
palavra_certa = '' #quantitade de vezes que a palavra está correta
tentativa = 0
while True:
    letra = str(input("\033[31mDigite uma letra \033[m: ")).lower()[0] #pega a primeira letra
    tentativa += 1

    if letra in palavra:
        palavra_certa += letra # recebe as letras corretas

    palavra_final = '' #juntando as palavras
    for c in palavra:
        if c in palavra_certa:
            palavra_final += c
        else:
            palavra_final += '*'
    
    print('palavra formada', palavra_final) #mostra a formação da palavra
    if palavra_final == palavra:
        system('cls')
        print(f"Parabens você acertou! A palavra era {palavra}")
        print("Número de tentativas", tentativa)
        break
