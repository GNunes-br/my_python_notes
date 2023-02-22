# FUNÇÕES
# REF.: https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions

# A palavra reservada def inicia a definição de uma função. Ela deve ser seguida do nome da função e da lista de parâmetros formais entre parênteses.
# Os comandos que formam o corpo da função começam na linha seguinte e devem ser indentados.

# Opcionalmente, a primeira linha do corpo da função pode ser uma literal string, cujo propósito é documentar a função. Se presente, essa string chama-se docstring.
# Existem ferramentas que utilizam docstrings para produzir automaticamente documentação online ou para imprimir,
# ou ainda, permitir que o usuário navegue interativamente pelo código.
# É uma boa prática incluir sempre docstrings em suas funções, portanto, tente fazer disso um hábito.

def printNome(nome: str) -> None:
    '''Esse método imprime o nome do usuário'''
    print('Nome:', nome)

printNome('Guilherme')
# Guilherme

# A execução de uma função cria uma nova tabela de símbolos para as variáveis locais da função.
# Mais precisamente, todas as atribuições de variáveis numa função são armazenadas na tabela de símbolos local;
# referências a variáveis são buscadas primeiro na tabela de símbolos local, em seguida na tabela de símbolos locais de funções delimitadoras ou circundantes,
# depois na tabela de símbolos global e, finalmente, na tabela de nomes da própria linguagem.
# Embora possam ser referenciadas, variáveis globais e de funções externas não podem ter atribuições
# (a menos que seja utilizado o comando global, para variáveis globais,
# ou nonlocal, para variáveis de funções externas).

# Os parâmetros reais (argumentos) de uma chamada de função são introduzidos na tabela de símbolos local da função no momento da chamada;
# portanto, argumentos são passados por valor (onde o valor é sempre uma referência para objeto, não o valor do objeto).
# Quando uma função chama outra função, ou chama a si mesma recursivamente, uma nova tabela de símbolos é criada para tal chamada.

# Uma definição de função associa o nome da função com o objeto função na tabela de símbolos atual.
# O interpretador reconhece o objeto apontado pelo nome como uma função definida pelo usuário.
# Outros nomes também podem apontar para o mesmo objeto função e também pode ser usados pra acessar a função:

print(printNome)
# <function printNome at 0x0000020167BCFC40>

f = printNome

f('Guilherme')
# Guilherme

# Conhecendo outras linguagens, pode-se questionar que fib não é uma função, mas um procedimento,
# pois ela não devolve um valor. Na verdade, mesmo funções que não usam o comando return devolvem um valor,
# ainda que pouco interessante. Esse valor é chamado None (é um nome embutido).
# O interpretador interativo evita escrever None quando ele é o único resultado de uma expressão. Mas se quiser vê-lo pode usar a função print():

print(printNome('Guilherme'))
# None

# É possível definir funções com um número variável de argumentos. Existem três formas, que podem ser combinadas.

# Argumentos com valor padrão

# A mais útil das três é especificar um valor padrão para um ou mais argumentos.
# Isso cria uma função que pode ser invocada com menos argumentos do que os que foram definidos.

def printUsuario(idade, nome = 'Guilherme', peso = 70):
    print('Idade:',idade,'\nNome:',nome,'\nPeso:', peso)

printUsuario(21)
# Idade: 21
# Nome: Guilherme
# Peso: 70

# Essa função pode ser chamada de várias formas.
# 1. fornecendo apenas o argumento obrigatório: printUsuario(18)
# 2. fornecendo um dos argumentos opcionais: printUsuario(18, 'Joao')
# 3. ou fornecendo todos os argumentos: printUsuario(18, 'Joao', 72)

# Os valores padrões são avaliados no momento da definição da função, e no escopo em que a função foi definida, portanto:

i = 5

def f(arg=i):
    print(arg)

i = 6

f()
# 5

# Aviso importante: Valores padrões são avaliados apenas uma vez. Isso faz diferença quando o valor é um objeto mutável,
# como uma lista, dicionário, ou instâncias de classes. Por exemplo, a função a seguir acumula os argumentos passados,
# nas chamadas subsequentes:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
# [1]
print(f(2))
# [1, 2]
print(f(3))
# [1, 2, 3]

# Se não quiser que o valor padrão seja compartilhado entre chamadas subsequentes, pode reescrever a função assim:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
# [1]
print(f(2))
# [2]
print(f(3))
# [3]

# Argumentos nomeados

# Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor. Por exemplo, a função a seguir:

printUsuario(18, peso=75, nome='Joao')
# Idade: 18
# Nome: Guilherme
# Peso: 75

# Em uma chamada de função, argumentos nomeados devem vir depois dos argumentos posicionais.
# Todos os argumentos nomeados passados devem corresponder com argumentos aceitos pela função

# Quando um último parâmetro formal no formato **nome está presente, ele recebe um dicionário contendo todos os argumentos nomeados,
# exceto aqueles que correspondem a um parâmetro formal. Isto pode ser combinado com um parâmetro formal no formato *nome (descrito na próxima subseção)
# que recebe uma tupla contendo os argumentos posicionais, além da lista de parâmetros formais. (*nome deve ocorrer antes de **nome.)
# Por exemplo, se definirmos uma função assim:

def printUsuario(idade, *arguments, **keywords):
    print(arguments[0])
    print('Idade:',idade,'\nNome:',keywords['nome'],'\nPeso:', keywords['peso'])

printUsuario(21, 'Detalhes do usuário', nome='Joao', peso=75)
# Detalhes do usuário
# Idade: 21
# Nome: Joao
# Peso: 75

# Parametros especiais

# Por padrão, argumentos podem ser passadas para uma função Python tanto por posição quanto explicitamente pelo nome.
# Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados,
# assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    #   -----------    ----------     ----------
    #        |             |                  |
    #        |        Positional or keyword   |
    #        |                                |  - Keyword only
    #        | - Positional only

def printUsuario(idade, /, peso, *, nome):
    print('Idade:',idade,'\nNome:',nome,'\nPeso:', peso)

printUsuario(18,75,nome='Guilherme')

