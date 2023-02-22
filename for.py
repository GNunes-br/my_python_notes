# COMANDO FOR
# REF.: https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements

# O comando for em Python é um pouco diferente do que costuma ser em C ou Pascal.
# Ao invés de sempre iterar sobre uma progressão aritmética de números (como no Pascal),
# ou permitir ao usuário definir o passo de iteração e a condição de parada (como C), o comando for do Python itera 
# sobre os itens de qualquer sequência (seja uma lista ou uma string), na ordem que aparecem na sequência. Por exemplo:

numeros = [1,2,3,4]

for numero in numeros:
    print(numero)

# OBS.:
# * Código que modifica uma coleção sobre a qual está iterando pode ser inseguro.
# No lugar disso, usualmente você deve iterar sobre uma cópia da coleção ou criar uma nova coleção:

usuarios = {
    'Guilherme': 'ativo',
    'Maria': 'ativo',
    'Joao': 'inativo'
}

for usuario, status in usuarios.copy().items():
    if(status == 'inativo'):
        del usuarios[usuario]

print(usuarios)
# {'Guilherme': 'ativo', 'Maria': 'ativo'}

usuarios_ativos = {}
for usuario, status in usuarios.items():
    if(status == 'ativo'):
        usuarios_ativos[usuario] = status

print(usuarios_ativos)
# {'Guilherme': 'ativo', 'Maria': 'ativo'}
