# TESTE DO VALOR VERDADE
# REF.: https://docs.python.org/pt-br/3/library/stdtypes.html#truth-value-testing

# Por padrão, um objeto é considerado verdadeiro, a menos que sua a classe defina um método __bool__()
# que retorne False ou um método __len__() que retorna zero, quando chamado com o objeto.
# Aqui estão a maioria dos objetos embutidos considerados falsos:
#   * Constantes definidas para serem falsas: None e False.
#   * Zero de qualquer tipo numérico: 0, 0.0, 0j, Decimal(0), Fraction(0, 1).
#   * Sequências e coleções vazias: '', (), [], {}, set(), range(0).

if None:
    print('Hello World') # Não será executado

if False:
    print('Hello World') # Não será executado

if 0:
    print('Hello World') # Não será executado

if 0.0:
    print('Hello World') # Não será executado

if []:
    print('Hello World') # Não será executado

if ():
    print('Hello World') # Não será executado

if {}:
    print('Hello World') # Não será executado

if set():
    print('Hello World') # Não será executado

if range(0):
    print('Hello World') # Não será executado

# Operações e funções embutidas que têm um resultado Booleano
# retornam 0 ou False para falso e 1 ou True para verdadeiro, salvo indicações ao contrário.
# (Exceção importante: as operações Booleanas or e and sempre retornam um de seus operandos).

if 1:
    print('Hello World')
    # Hello World
