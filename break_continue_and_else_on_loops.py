# COMANDOS BREAK, CONTINUE AND ELSE NOS LAÇOS DE REPETIÇÃO
# REF.: https://docs.python.org/pt-br/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

# O comando break, como no C, sai imediatamente do laço de repetição mais interno, seja for ou while.

# Laços podem ter uma cláusula else, que é executada sempre que o laço se encerra por exaustão do iterável (no caso do for)
# ou quando a condição se torna falsa (no caso do while), mas nunca quando o laço é interrompido por um break.
# Isto é exemplificado no próximo exemplo que procura números primos.

for numero in range(2, 10):
    for aux in range(2, numero):
        if (numero % aux == 0):
            print(numero, 'igual', aux, '*', numero // aux)
            break
    else:
        print(numero, 'é um número primo')

# 2 é um número primo
# 3 é um número primo
# 4 igual 2 * 2
# 5 é um número primo
# 6 igual 2 * 3
# 7 é um número primo
# 8 igual 2 * 4
# 9 igual 3 * 3

# Quando usado em um laço, a cláusula else tem mais em comum com a cláusula else de um comando try
# do que com a de um comando if: a cláusula else de um comando try executa quando não ocorre exceção,
# e o else de um laço executa quando não ocorre um break.

# A instrução continue, também emprestada da linguagem C, continua com a próxima iteração do laço.

for numero in range(2, 10):
    if numero % 2 == 0:
        print('Encontrou um número par', numero)
        continue

    print('Encontrou um número ímpar', numero)

# Encontrou um número par 2
# Encontrou um número ímpar 3
# Encontrou um número par 4
# Encontrou um número ímpar 5
# Encontrou um número par 6
# Encontrou um número ímpar 7
# Encontrou um número par 8
# Encontrou um número ímpar 9