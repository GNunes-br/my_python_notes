# RANGE
# REF.: https://docs.python.org/pt-br/3/tutorial/controlflow.html#the-range-function

# Se você precisa iterar sobre sequências numéricas, a função embutida range() é a resposta. Ela gera progressões aritméticas.

for i in range(5):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4

# O ponto de parada fornecido nunca é incluído na lista;
# range(10) gera uma lista com 10 valores, exatamente os índices válidos para uma sequência de comprimento 10.
# É possível iniciar o intervalo com outro número, ou alterar a razão da progressão (inclusive com passo negativo).

for i in range(5, 10):
    print(i)
    # 5
    # 6
    # 7
    # 8
    # 9

for i in range(0, 10, 3):
    print(i)
    # 0
    # 3
    # 6
    # 9

for i in range(-10, -100, -30):
    print(i)
    # -10
    # -40
    # -70

# Para iterar sobre os índices de uma sequência, combine range() e len() da seguinte forma.

usuarios = ['Guilherme', 'Joao', 'Maria']

for i in range(len(usuarios)):
    print(i, usuarios[i])
    # 0 Guilherme
    # 1 Joao
    # 2 Maria