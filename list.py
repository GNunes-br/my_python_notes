# LISTAS
# REF.: https://docs.python.org/pt-br/3/tutorial/introduction.html#lists

# Python inclui diversas estruturas de dados compostas, usadas para agrupar outros valores.
# A mais versátil é list (lista), que pode ser escrita como uma lista de valores (itens) separados por vírgula,
# entre colchetes. Os valores contidos na lista não precisam ser todos do mesmo tipo.

numeros = [1,2,5,4,8,6]
print(numeros)
# [1, 2, 5, 4, 8, 6]

numeros = [1, 2, 'World!', 4, 8, 'Hello']
print(numeros)
# [1, 2, 'World!', 4, 8, 'Hello']

# Como strings (e todos os tipos embutidos de sequência), listas pode ser indexados e fatiados.
numeros = [1,2,5,4,8,'Hello', 'World']

print(numeros[0])
# 1

print(numeros[-1])
# World

print(numeros[-3:]) # Retorna uma lista
# [8, 'Hello', 'World']

# OBS.:
# Todas as operações de fatiamento devolvem uma nova lista contendo os elementos solicitados.
# Isso significa que o seguinte fatiamento devolve uma cópia rasa da lista.

print(numeros[:])
# [1, 2, 5, 4, 8, 'Hello', 'World']

# As listas também suportam operações como concatenação:
numeros = [1,2,3,4,5,6]
palavras = ['Hello', 'World']

print(numeros + palavras)
# [1, 2, 3, 4, 5, 6, 'Hello', 'World']

# Diferentemente de strings, que são imutáveis, listas são mutáveis, ou seja, é possível alterar elementos individuais de uma lista.
numeros = [1,2,3,4,5,6]

numeros[0] = 2
numeros[1] = 3

print(numeros)
# [2, 3, 3, 4, 5, 6]

# Você também pode adicionar novos itens no final da lista, usando o método append()

numeros = []

numeros.append(1)
numeros.append(2)
numeros.append(3)

print(numeros)
# [1, 2, 3]

# Atribuição a fatias também é possível, e isso pode até alterar o tamanho da lista ou remover todos os itens dela.

numeros = [1,2,3,4,5]

numeros[2:3] = [10, 11]

print(numeros)
# [1, 2, 10, 11, 4, 5]

numeros[2:3] = []

print(numeros)
# [1, 2, 11, 4, 5]

numeros[-1:] = [20,30,40,50]
# [1, 2, 11, 4, 20, 30, 40, 50]

print(numeros)

numeros[:] = []

print(numeros)
# []

# A função embutida len() também se aplica a listas.
numeros = [1,2,3,4,5]

print(len(numeros))
# 5

# É possível aninhar listas (criar listas contendo outras listas)

numeros = [1,2,3,4,5,6]
palavras = ['Hello', 'World']

numeros_e_palavras = [numeros, palavras]

print(numeros_e_palavras)
# [[1, 2, 3, 4, 5, 6], ['Hello', 'World']]

print(numeros_e_palavras[0])
# [1, 2, 3, 4, 5, 6]

print(numeros_e_palavras[1])
# ['Hello', 'World']

print(numeros_e_palavras[1][1])
# World