# OPERAÇÕES BOOLEANAS - and, or, not
# REF.: https://docs.python.org/pt-br/3/library/stdtypes.html#boolean-operations-and-or-not

# Esses são as operações booleanas, ordenados por prioridade ascendente.
# x or y             ->          Se x é falso, então y, do contrário x
# x and y            ->          Se x é falso, então x, do contrário y
# not x              ->          Se x é falso, então True, caso contrário False

print(False or 'Hello World')
# Hello World

print('Hello' or 'World')
# Hello

print(False and 'Hello World')
# False

print(True and 'Hello World')
# Hello World

print(not 'Hello World')
# False

print(not False)
# True

# OBS.:
# * (x or y) é um operador de curto-circuito, por isso só avalia o segundo argumento se o primeiro é falso.
# * (x and y) é um operador de curto-circuito, por isso só avalia o segundo argumento se o primeiro é verdadeiro.
# * not tem uma prioridade mais baixa do que operadores não booleanos,
#   então not a == b é interpretado como not (a == b) e a == not b é um erro de sintaxe.