# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

ARQUIVO = 'ex21.json'

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Bababui', 22)
# p2 = Pessoa('Sus', 13)
# p3 = Pessoa('Cleitin', 19)
# dados = [p1.__dict__ ,p2.__dict__, p3.__dict__]
dados = p1.__dict__

def make_dump():
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo)