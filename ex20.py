# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

def listar(lista):
    print("\nTAREFAS\n")
    for itens in lista:
        print(itens)
    print()


def desfazer(item):
    refeitas.append(item)
    return refeitas


def refazer(item):
    item.append(refeitas[-1])
    return item


todo = []
refeitas = []

while True:
    print("Comandos => listar, desfazer, refazer, stop")
    tarefa = str(input('Digite uma atividade ou um comando: '))
    print()

    if tarefa == 'listar':
        listar(todo)
    elif tarefa == 'desfazer':
        print(desfazer(todo[-1]))
        todo.pop()
    elif tarefa == 'refazer':
        refazer(todo)
    elif tarefa == 'clear':
        os.system('cls')
    elif tarefa == 'stop':
        break
    else:
        todo.append(tarefa)
