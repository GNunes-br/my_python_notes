# MATCH
# REF.: https://docs.python.org/pt-br/3/tutorial/controlflow.html#match-statements

# Uma instrução match pega uma expressão e compara seu valor com padrões sucessivos fornecidos como um ou mais blocos de case.
# Isso é superficialmente semelhante a uma instrução switch em C, Java ou JavaScript (e muitas outras linguagens),
# mas também pode extrair componentes (elementos de sequência ou atributos de objeto) do valor em variáveis,
# mas muito mais parecido com a correspondência de padrões em linguages como Rust ou Haskell.
# Apenas o primeiro padrão que corresponder será executado, podendo também extrair componentes
# (elementos de sequência ou atributos de objetos) do valor para variáveis

def erroHttp(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(erroHttp(400))
# Bad request
        
print(erroHttp(500))
# Something's wrong with the internet

# Observe o último bloco: o “nome da variável” _ atua como um curinga e nunca falha em corresponder.
# Se nenhum caso corresponder, nenhuma das ramificações será executada.

# Você pode combinar vários literais em um único padrão usando | (“ou”).

def erroHttp(status):
    match status:
        case 400 | 401 | 404:
            return 'Not allowed'
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(erroHttp(401))
# Not allowed

# Os padrões podem se parecer com atribuições de desempacotamento e podem ser usados para vincular variáveis.

x = 0
y = 5
pontoCartesiano = (x,y)
match pontoCartesiano:
    case (0,0):
        print('Origem')
    case (0, y):
        print(f'Y = {y}')
    case (x, 0):
        print(f'X = {x}')
    case (x, y):
        print(f'X = {x}, Y={y}')
    case _:
        raise ValueError("Not a point")

# Y = 5

# Estude isso com cuidado! O primeiro padrão tem dois literais e pode ser considerado uma extensão do padrão literal mostrado acima.
# Mas os próximos dois padrões combinam um literal e uma variável, e a variável vincula um valor do assunto (pontoCartesiano).
# O quarto padrão captura dois valores, o que o torna conceitualmente semelhante à atribuição de desempacotamento (x, y) = pontoCartesiano.

# Se você estiver usando classes para estruturar seus dados, você pode usar o nome da classe seguido por uma lista de argumentos
# semelhante a um construtor, mas com a capacidade de capturar atributos em variáveis.

class PontoCartesiano:
    y: int
    x: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def ondeEsta(pontoCartesiano):
    match pontoCartesiano:
        case PontoCartesiano(x=0, y=0):
            print('Origem')
        case PontoCartesiano(x=0, y=y):
            print(f"Y={y}")
        case PontoCartesiano(x=x, y=0):
            print(f"X={x}")
        case PontoCartesiano():
            print("Em outro lugar")
        case _:
            print("Não é um ponto")

ondeEsta(PontoCartesiano(0,0))
# Origem

ondeEsta(PontoCartesiano(0,7))
# Y=7

# Uma maneira recomendada de ler padrões é vê-los como uma forma estendida do que você colocaria à esquerda de uma atribuição,
# para entender quais variáveis seriam definidas para quê. Apenas os nomes autônomos (como var acima) são atribuídos
# por uma instrução de correspondência. Nomes pontilhados (como foo.bar), nomes de atributos (o x= e y= acima) ou nomes de
# classes (reconhecidos pelo “(…)” próximo a eles, como Point acima) nunca são atribuídos.

# Os padrões podem ser aninhados arbitrariamente. Por exemplo, se tivermos uma pequena lista de pontos.

x = 0
y = 1
x2 = 0
y2 = 1
pontosCartesiano = [
    PontoCartesiano(x=x,y=y),
    PontoCartesiano(x=x2,y=y2)
]
match pontosCartesiano:
    case []:
        print('Não há pontos')
    case [PontoCartesiano(x=0 , y=0)]:
        print('A origem')
    case [PontoCartesiano(x=x, y=y)]:
        print(f"Ponto simples {x}, {y}")
    case [PontoCartesiano(x=0, y=y), PontoCartesiano(x=0, y=y2)]:
        print(f"Dois pontos no eixo Y em {y}, {y2}")
    case _:
            print("Em outro lugar")

# Dois pontos no eixo Y em 1, 1

# Podemos adicionar uma cláusula if a um padrão, conhecido como “guarda”.
# Se a guarda for falsa, match continua para tentar o próximo bloco de caso.
# Observe que a captura de valor ocorre antes que a guarda seja avaliada

x = 5
y = 5
pontoCartesiano = PontoCartesiano(x=x, y=y)
match pontoCartesiano:
    case PontoCartesiano(x=x, y=y) if x == y:
        print(f'Y=X em {x}')
    case PontoCartesiano(x=x, y=y):
        print('Não na diagonal')

# Y=X em 5