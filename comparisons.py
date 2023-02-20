# COMPARAÇÕES
# REF.: https://docs.python.org/pt-br/3/library/stdtypes.html#comparisons

# Há oito operadores comparativos no Python.
# Todos eles possuem a mesma prioridade (que é maior do que aquela das operações Booleanas).
# Comparações podem ser encadeadas arbitrariamente; por exemplo, x < y <= z é equivalente a x < y and y <= z,
# exceto que y é avaliado apenas uma vez (porém em ambos os casos z não é avaliado de todo quando x < y é sabido ser falso).

x = 1
y = 2
z = 3

print(x < y <= z)
# True

print(x < y and y <= z)
# True

print(x > y <= z)
# False

# Esses são as operações booleanas, ordenados por prioridade ascendente.
# <             ->          Estritamente menor que
# <=            ->          Menor que ou igual
# >             ->          Eestritamente maior que
# >=            ->          Maior que ou igual
# ==            ->          Igual
# !=            ->          Não é igual
# is            ->          Identidade do objeto
# is not        ->          Identidade de objeto negada

print(1 < 2)
# True

print(3 < 2)
# False

print(3 > 2)
# True

print(1 > 2)
# False

print(1 <= 2)
# True

print(3 <= 2)
# False

print(2 <= 2)
# True

print(3 >= 2)
# True

print(1 >= 2)
# False

print(2 >= 2)
# True

print(2 == 2)
# True

print(1 == 2)
# False

print(1 != 2)
# True

print(2 != 2)
# False

print(type(0) is type('0'))
# False

print(type(0) is type(0))
# True

print(type('Hello World') is not type(0))
# True

print(type('Hello World') is not type('0'))
# False

# Objetos de tipos diferentes, exceto tipos numéricos diferentes, nunca comparam iguais.
# O operador == é sempre definido, mas para alguns tipos de objetos (por exemplo, objetos de classe) é equivalente a is.
# Os operadores <, <=, > e >= são definidos apenas onde fazem sentido;
# por exemplo, eles levantam uma exceção TypeError quando um dos argumentos é um número complexo.

print(type(0) == type('0'))
# False

print(type(0) == type(0))
# True

# Instâncias não idênticas de uma classe normalmente comparam-se como desiguais ao menos que a classe defina o método __eq__().

print(str('Hello World') is str('World Hello'))
# False

# Instâncias de uma classe não podem ser ordenadas com respeito a outras instâncias da mesma classe,
# ou outros tipos de objeto, ao menos que a classe defina o suficiente dos métodos
# __lt__(), __le__(), __gt__() e __ge__() (no geral, __lt__() e __eq__() são suficientes,
# se você quiser o significado convencional dos operadores de comparação).

# O comportamento dos operadores is e is not não pode ser personalizado;
# além disso eles podem ser aplicados a quaisquer dois objetos e nunca levantam uma exceção.

# Mais duas operações com a mesma prioridade sintática, in e not in,
# são suportadas por tipos que são iteráveis ou implementam o método __contains__().