# PACOTES
# REF.: https://docs.python.org/pt-br/3/tutorial/modules.html#packages

# Os pacotes são uma maneira de estruturar o “espaço de nomes” dos módulos Python, usando “nomes de módulo com pontos”.
# Por exemplo, o nome do módulo A.B designa um submódulo chamado B, em um pacote chamado A.
# Assim como o uso de módulos evita que os autores de módulos diferentes tenham que se preocupar com nomes de variáveis globais,
# o uso de nomes de módulos com pontos evita que os autores de pacotes com muitos módulos, como NumPy ou Pillow,
# tenham que se preocupar com os nomes dos módulos uns dos outros.

# Suponha que você queira projetar uma coleção de módulos (um “pacote”) para o gerenciamento uniforme de arquivos de som.
# Existem muitos formatos diferentes (normalmente identificados pela extensão do nome de arquivo, por exemplo .wav, .aiff, .au),
# de forma que você pode precisar criar e manter uma crescente coleção de módulos de conversão entre formatos.
# Ainda podem existir muitas operações diferentes, passíveis de aplicação sobre os arquivos de som (mixagem, eco, equalização, efeito stereo artificial).
# Logo, possivelmente você também estará escrevendo uma coleção sempre crescente de módulos para aplicar estas operações.
# Eis uma possível estrutura para o seu pacote (expressa em termos de um sistema de arquivos hierárquico):

# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# Ao importar esse pacote, Python busca pelo subdiretório com mesmo nome, nos diretórios listados em sys.path.

# Os arquivos __init__.py são necessários para que o Python trate diretórios contendo o arquivo como pacotes.
# Isso previne que diretórios com um nome comum, como string, ocultem, involuntariamente, módulos válidos que ocorrem
# posteriormente no caminho de busca do módulo. No caso mais simples, __init__.py pode ser apenas um arquivo vazio,
# mas pode também executar código de inicialização do pacote, ou configurar a variável __all__, descrita mais adiante.

# Usuários do pacote podem importar módulos individuais, por exemplo:

import sound.effects.echo

# Isso carrega o submódulo sound.effects.echo. Ele deve ser referenciado com seu nome completo, como em:

sound.effects.echo.echofilter('input', 'output', delay=0.7, atten=4)
# ('input', 'output')
# {'delay': 0.7, 'atten': 4}

# Uma maneira alternativa para a importação desse módulo é:

from sound.effects import echo

# Isso carrega o submódulo echo sem necessidade de mencionar o prefixo do pacote no momento da utilização, assim:

echo.echofilter('input', 'output', delay=0.7, atten=4)
# ('input', 'output')
# {'delay': 0.7, 'atten': 4}

# Também é possível importar diretamente uma única variável ou função:

from sound.effects.echo import echofilter

# Novamente, isso carrega o submódulo echo, mas a função echofilter() está acessível diretamente sem prefixo:

echofilter('input', 'output', delay=0.7, atten=4)
# ('input', 'output')
# {'delay': 0.7, 'atten': 4}

# Observe que ao utilizar from pacote import item, o item pode ser um subpacote, submódulo, classe, função ou variável.
# O comando import primeiro testa se o item está definido no pacote, senão assume que é um módulo e tenta carregá-lo.
# Se falhar em encontrar o módulo, uma exceção ImportError é levantada.

# Em oposição, em uma construção como import item.subitem.subsubitem, cada item, com exceção do último, deve ser um pacote.
# O último pode ser também um pacote ou módulo, mas nunca uma classe, função ou variável contida em um módulo

# Importando * de um pacote

# Agora, o que acontece quando um usuário escreve from sound.effects import * ? Idealmente, poderia se esperar
# que este comando vasculhasse o sistema de arquivos, encontrasse todos os submódulos presentes no pacote, e os importasse.
# Isso poderia demorar muito e a importação de submódulos pode ocasionar efeitos colaterais, que somente deveriam ocorrer
# quando o submódulo é explicitamente importado.

# A única solução é o autor do pacote fornecer um índice explícito do pacote. O comando import usa a seguinte convenção: se o arquivo __init__.py
# do pacote define uma lista chamada __all__, então esta lista indica os nomes dos módulos a serem importados quando o comando from pacote import * é acionado.
# Fica a cargo do autor do pacote manter esta lista atualizada, inclusive fica a seu critério excluir inteiramente o suporte a importação direta de
# todo o pacote através de from pacote import *. Por exemplo, o arquivo sounds/effects/__init__.py poderia conter apenas:

__all__ = ["echo", "surround", "reverse"]

# Isso significaria que from sound.effects import * importaria os três submódulos nomeados do pacote sound.effects.

# Se __all__ não estiver definido, o comando from sound.effects import * não importa todos os submódulos do pacote sound.effects no espaço de nomes atual.
# Há apenas garantia que o pacote sound.effects foi importado (possivelmente executando qualquer código de inicialização em __init__.py)
# juntamente com os nomes definidos no pacote. Isso inclui todo nome definido em __init__.py bem como em qualquer submódulo importado a partir deste.
# Também inclui quaisquer submódulos do pacote que tenham sido carregados explicitamente por comandos import anteriores. Considere o código abaixo:

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

# Nesse exemplo, os nomes echo e surround são importados no espaço de nomes atual, no momento em que o comando from...import é executado,
# pois estão definidos no pacote sound.effects. (Isso também funciona quando __all__ estiver definida.)

# Apesar de que certos módulos são projetados para exportar apenas nomes conforme algum critério quando se faz import *,
# ainda assim essa sintaxe é considerada uma prática ruim em código de produção.

# Lembre-se, não há nada errado em usar from pacote import submodulo_especifico! De fato, essa é a notação recomendada,
# a menos que o módulo importado necessite usar submódulos com o mesmo nome, de diferentes pacotes.

# Referências em um mesmo pacote

# Quando pacotes são estruturados em subpacotes (como no pacote sound do exemplo), pode-se usar a sintaxe de importações absolutas
# para se referir aos submódulos de pacotes irmãos (o que na prática é uma forma de fazer um import relativo, a partir da base do pacote).
# Por exemplo, se o módulo sound.filters.vocoder precisa usar o módulo echo do pacote sound.effects, é preciso importá-lo com from sound.effects import echo.

# Também é possível escrever imports relativos, com a forma from modulo import nome. Esses imports usam pontos para indicar o
# pacote pai e o atual, envolvidos no import relativo. Do módulo surround, por exemplo, pode-se usar:

# from . import echo
# from .. import format
# from ..filters import equalizer

# Pacotes em múltiplos diretórios

# Pacotes possuem mais um atributo especial, __path__. Inicializado como uma lista contendo o nome do diretório onde está o arquivo __init__.py
# do pacote, antes do código naquele arquivo ser executado. Esta variável pode ser modificada; isso afeta a busca futura de módulos e subpacotes contidos no pacote.

# Apesar de não ser muito usado, esse mecanismo permite estender o conjunto de módulos encontrados em um pacote.
