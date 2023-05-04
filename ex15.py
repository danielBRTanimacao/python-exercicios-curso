from os import system

perguntas = [
    {
        'pergunta': 'Quanto e 1 + 1 = ?',
        'opções': ['1', '2', '4', '11'], 
        'resposta': '1',
    },
    {
        'pergunta': 'Quantos dias são necessários para a Terra orbitar o sol?',
        'opções': ['365', '120', '1', '366'], 
        'resposta': '0',
    },
    {
        'pergunta': 'De qual cidade vieram os Beatles?',
        'opções': ['Moscow', 'Rio de Janeiro', 'Bababui', 'nenhuma das alternativas'], 
        'resposta': '3',
    }
]
certo = 0
for per in perguntas:
    print(f"Pergunta {per['pergunta']}\n")
    for num, op in enumerate(per['opções']):
        print(f"{num}) {op}")
    resp = input(f"Escolha alternativa: ")
    if resp == per['resposta']:
        print("\033[32mAcertou\033[m\n")
        certo += 1
    else:
        print("\033[31mErrou\033[m\n")
system('cls')
print("="*42)
print(f"Parabens você acertou {certo}!".center(42))
print("="*42)