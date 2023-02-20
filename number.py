# NUMEROS
# REF.: https://docs.python.org/pt-br/3/tutorial/introduction.html#numbers

# O interpretador funciona como uma calculadora bem simples: 
# você pode digitar uma expressão e o resultado será apresentado.
# A sintaxe de expressões é a usual: operadores +, -, * e / funcionam da mesma forma que em outras linguagens tradicionais (por exemplo, Pascal ou C);
# parênteses (()) podem ser usados para agrupar expressões. Por exemplo:

# Os números inteiros (ex. 2, 4, 20) são do tipo int, aqueles com parte fracionária (ex. 5.0, 1.6) são do tipo float.

print(2 + 2.0)
# 4.0

print(2 + 2)
# 4

print(2 + 2.5)
# 4.5

print(50 - 5 * 6)
# 20

print((50 - 5 * 6) / 4)
# 5.0

print(8 / 5)
# 1.6

# OBS.:
# * Divisões sempre retornam um número co ponto flutuante
# * Para fazer uma divisão pelo piso e receber um inteiro como resultado você pode usar o operador //.
# * Para calcular o resto você pode usar o %.
# * É possível usar o operador ** para calcular potências

print(8 // 4)
# 2

print(8 // 5)
# 1

print(17 % 3)
# 2

print(5 ** 2)
# 25

# Tipos de operações
# x + y             ->          Soma de x e y
# x - y             ->          Diferença de x e y
# x * y             ->          Produto de x + y
# x / y             ->          Quociente de x + y
# x // y            ->          Piso do quociente de x + y
# x % y             ->          Restante de x / y
# -x                ->          x negado
# +x                ->          x inalterado
# abs(x)            ->          Valor absoluto ou magnitude de x
# int(x)            ->          x convertido em inteiro
# float(x)          ->          x convertido em ponto flutuante
# complex(re, im)   ->          Um número complexo com parte real re, parte imaginária im. im tem como padrão zero
# c.conjugate()     ->          Conjugado do número complexo c
# divmod(x, y)      ->          O par (x // y, x % y)
# pow(x, y)         ->          x elevado a y
# x ** y            ->          x elevado a y

# OBS.:
# * Também referido como uma divisão inteira. O valor resultante é um integral inteiro,
#   embora o tipo oriundo do resultado não seja necessariamente int.
#   O resultado é sempre arredondado para menos infinito: 1//2 é 0, (-1)//2 é -1, 1//(-2) é -1 e (-1)//(-2) é 0.
# * Ponto flutuante também aceita a string “nan” e “inf” com um prefixo opcional “+” ou “-” a Não é um Número (NaN)
#   e infinidade positiva ou negativa.
# * Python define pow(0, 0) e 0 ** 0 sendo 1, como é comum para linguagens de programação.
# * Os literais numéricos aceitos incluem os dígitos de 0 a 9 ou qualquer equivalente Unicode (pontos de código com a propriedade Nd).