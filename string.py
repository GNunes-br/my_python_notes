# TEXTOS
# REF.: https://docs.python.org/pt-br/3/tutorial/introduction.html#strings

# Python também pode manipular strings (sequências de caracteres), que podem ser expressas de diversas formas.
# Elas podem ser delimitadas por aspas simples ('...') ou duplas ("..."). \ pode ser usada para escapar aspas.

# Aspas simples
texto = 'Hello World!'
print(texto)
# Hello World!

# Uso de \ para uso de aspas simples em um texto com aspas simples
texto = 'Exemplo do uso de \' dentro de uma string definida com aspas simples'
print(texto)
# Exemplo do uso de ' dentro de uma string definida com aspas simples

# Uso de aspas simples em um texto com aspas duplas
texto = "Exemplo do uso de ' dentro de uma string definida com aspas duplas"
print(texto)
# Exemplo do uso de ' dentro de uma string definida com aspas simples

# Uso de aspas duplas em um texto com aspas simples
texto = 'Exemplo do uso de " dentro de uma string definida com aspas simples'
print(texto)
# Exemplo do uso de " dentro de uma string definida com aspas simples

# As strings literais podem abranger várias linhas.
# Uma maneira é usar as aspas triplas: """...""" ou '''...'''.
# O fim das linhas é incluído automaticamente na string, mas é possível evitar isso adicionando uma \ no final.

texto = '''
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
    It has survived not only five centuries, but also the leap into electronic typesetting,
    remaining essentially unchanged.It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
'''
print(texto)

# Strings podem ser concatenadas (coladas) com o operador +, e repetidas com *:
texto ='Ba', 2 * 'na'
print(texto, sep='')
# Banana

# Duas ou mais strings literais (ou seja, entre aspas) ao lado da outra são automaticamente concatenados.
texto = 'Py' 'thon'
print(texto)
# Python

texto = (
    'Essa é a primeira linha '
    'Essa é a segunda linha'
)
print(texto)
# Essa é a primeira linha Essa é a segunda linha

# OBS.:
# * Isso só funciona com duas strings literais, não com variáveis ou expressõe. Exemplo: ... return variavel 'string'

# Se você quiser concatenar variáveis ou uma variável e uma literal, use +.
texto = 'Py' + 'thon'
print(texto)
# Python

# As strings podem ser indexadas (subscritas), com o primeiro caractere como índice 0 (Não existe um tipo específico para caracteres);
# Um caractere é simplesmente uma string cujo tamanho é 1:

texto = 'Python'
print(texto[0])
# P

print(texto[1])
# y

print(texto[3])
# h

print(texto[-1])
# n

print(texto[-2])
# o

# OBS.:
# * Índices também podem ser números negativos para iniciar a contagem pela direita;
# * Note que dado que -0 é o mesmo que 0, índices negativos começam em -1.
# * A tentativa de usar um índice que seja muito grande resultará em um erro. Exemplo: ...print(texto[41])

# Os índices do fatiamento possuem padrões úteis;
# um primeiro índice omitido padrão é zero, um segundo índice omitido é por padrão o tamanho da string sendo fatiada.

texto = 'Hello World!'
print(texto[:2])
# He

print(texto[2:])
# llo World!

print(texto[1:3])
# el

print(texto[-4:])
# rld!

# Uma maneira de lembrar como fatias funcionam é pensar que os índices indicam posições entre caracteres, onde a borda esquerda do primeiro caractere é 0. 
# Assim,a borda direita do último caractere de uma string de comprimento n tem índice n, por exemplo:

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# Os índices de fatiamento fora do alcance são tratados graciosamente quando usados para fatiamento.
# Um índice maior que o comprimento é trocado pelo comprimento, um limite superior menor que o limite inferior produz uma string vazia

print(texto[4:42])
# o World!

print(texto[42:])
# (String vazia)

# As strings do Python não podem ser alteradas — uma string é imutável.
# Portanto, atribuir a uma posição indexada na sequência resulta em um erro. Exemplo: texto[42] = 'D'

# A função embutida len() devolve o comprimento de uma string.

texto = '''
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    when an unknown printer took a galley of type and scrambled it to make a type specimen book.
    It has survived not only five centuries, but also the leap into electronic typesetting,
    remaining essentially unchanged.It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
'''

print(len(texto))
# 599

texto = 'Hello World!'
print(len(texto))
# 12