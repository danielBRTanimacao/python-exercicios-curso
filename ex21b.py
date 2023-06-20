import json
from ex21 import ARQUIVO, Pessoa, make_dump

with open(ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
p1 = Pessoa(**dados)
print(p1.nome, p1.idade)