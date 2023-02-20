# OBS.:
# * No Python não é necessário informar o tipo da variável, sua tipagem é dinâmica.
# * Uma variável só passa a existir quando atribuímos um valor.
# * O Python utiliza por convenção o padrão Snake_Case para nomes de variáveis, mas é possível usar também o padrão CamelCase.
# * Podemos consultar o tipo da variável com a classe type(object).

# type(object)
# REF.: https://docs.python.org/pt-br/3.11/library/functions.html?highlight=type#type

idade = 18
print(type(idade))
# <class 'int'>

nome = 'Guilherme'
print(type(nome))
# <class 'str'>

nome = idade
print(type(nome))
# <class 'int'>

altura = 1.80
print(type(altura))
# <class 'float'>