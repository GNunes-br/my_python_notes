# print(*objects, sep=' ', end='\n', file=None, flush=False)
# REF.: https://docs.python.org/pt-br/3.11/library/functions.html?highlight=print#print

print('Hello World!')
# Hello World!

print('Hello World!', 'how are you?')
# Hello World! how are you?

print('Hello World', 'how are you?', sep='---')
# Hello World---how are you?

print('b', 'n', 'n', '', sep='a')
# banana

dia = '18'
mes = '02'
ano = '2023'
print(dia, mes, ano, sep='/')
# 18/02/2023

# OBS.
# * Por padrão, a função print utiliza a quebra de linha (\n) como último caracter
#   Podemos modificar esse comportamento com o parâmetro 'end='.
print('Vamos estudar', end=' ')
print('Python')
# Vamos estudar Python

print("Quantidade", end=': ')
print(40)
# Quantidade: 40

# F-string
print('Hello {}{}'.format('World', '!'))
# Hello World!

nome = 'Guilherme'
print(f'Olá {nome}, tudo bem?')
# Olá Guilherme, tudo bem?

# OBS.:
# * É possível adicionarmos separadores em um número passando o valor ':,' após a variável.
numero = 12156110
print(f'{numero:,}')
# 12,156,110

idade = 18
print(f'Você é maior de idade? {"Sim" if idade >= 18 else "Não"}')

# OBS.:
# * É possível colorir o valor impresos utilizando um código junto ao texto, abaixo a tabela de códigos.

# TABELA DE CÓDIGO PARA ALTERAR DE ESTILOS
#   ESC [ 0 m       # reset all (colors and brightness)
#   ESC [ 1 m       # bright
#   ESC [ 2 m       # dim (looks same as normal brightness)
#   ESC [ 22 m      # normal brightness

# FOREGROUND:
#   ESC [ 30 m      # black
#   ESC [ 31 m      # red
#   ESC [ 32 m      # green
#   ESC [ 33 m      # yellow
#   ESC [ 34 m      # blue
#   ESC [ 35 m      # magenta
#   ESC [ 36 m      # cyan
#   ESC [ 37 m      # white
#   ESC [ 39 m      # reset

# BACKGROUND
#   ESC [ 40 m      # black
#   ESC [ 41 m      # red
#   ESC [ 42 m      # green
#   ESC [ 43 m      # yellow
#   ESC [ 44 m      # blue
#   ESC [ 45 m      # magenta
#   ESC [ 46 m      # cyan
#   ESC [ 47 m      # white
#   ESC [ 49 m      # reset

# cursor positioning
#   ESC [ y;x H     # position cursor at x across, y down
#   ESC [ y;x f     # position cursor at x across, y down
#   ESC [ n A       # move cursor n lines up
#   ESC [ n B       # move cursor n lines down
#   ESC [ n C       # move cursor n characters forward
#   ESC [ n D       # move cursor n characters backward

# clear the screen
#   ESC [ mode J    # clear the screen

# clear the line
#   ESC [ mode K    # clear the line


print('\033[31mHello World')
# Hello World (Impresso com o texto na cor vermelha)