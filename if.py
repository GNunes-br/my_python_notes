# COMANDO IF
# REF.: https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements

idade = int(input('Informe a sua idade: '))

if (idade < 18): # Se idade for menor que 18
    print('Criança ou jovem')
elif (18 <= idade < 60): # Se idade for maior ou igual a 18 e menor que 60
    print('Adulto')
else: # Caso não entre em nunhuma das condições acima
    print('Idoso')

    
# Pode haver zero ou mais partes elif, e a parte else é opcional. A palavra-chave ‘elif’ é uma abreviação para ‘else if’,
# e é útil para evitar indentação excessiva. Uma sequência if … elif … elif … substitui os comandos switch ou case, encontrados em outras linguagens.

if (True): print('Hello World!')

if (False):
    print('Hello')
else:
    print('World!')