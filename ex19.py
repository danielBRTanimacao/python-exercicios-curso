"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

lista1 = [2, 4, 23, 2, 12, 0, 1]
lista2 = [1, 2, 3, 4, 6]

soma = [x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)]
print(soma)