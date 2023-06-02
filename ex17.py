# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

def aumento(x, y): #brincando com codigo / testes
    return (x * y) / 100 + y


porcentagem = 10
produtos = [ #produtos atuais
    {'nome': 'Produto 5', 'preco': aumento(porcentagem, 12)},
    {'nome': 'Produto 1', 'preco': f'{(porcentagem*22.32)/100+22.32:.2f}'},
    {'nome': 'Produto 3', 'preco': f'{(porcentagem*10.11)/100+10.11:.2f}'},
    {'nome': 'Produto 2', 'preco': f'{(porcentagem*105.87)/100+105.87:.2f}'},
    {'nome': 'Produto 4', 'preco': (porcentagem*69.90)/100+69.90},
]

novos_produtos = produtos.copy() #copia profunda mais novos produtos
novos_produtos.append({'nome': 'Produto 6', 'preco': aumento(porcentagem, 1.50)})

produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda item: item['nome'])
#produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda item: item['preco'])

# for items in novos_produtos:
#     print(items)

# for items in produtos_ordenados_por_preco:
#     print(items)
