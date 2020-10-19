"""
Módulo Collections - Counter

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

"""

# Realizando o import

from collections import Counter

# Dodemos utilziar qualquer iterável, e aqui utilizamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 5, 5, 1, 1, 12]
# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)
print()
print(Counter('Wellington e Tarcia'))

# Exemplo 2

texto = """George Harrison foi um guitarrista, cantor, compositor, produtor musical e cinematográfico inglês que obteve
fama internacional como guitarrista dos Beatles. Geralmente chamado de "o Beatle quieto", Harrison aderiu ao hinduísmo
 e ajudou a ampliar os horizontes dos outros Beatles assim como seu público ocidental ao incorporar instrumentos
indianos na música do grupo. Embora a maioria das canções da banda fossem escritas por John Lennon e Paul McCartney,
a maioria dos álbuns dos Beatles, a partir de 1965, continham, pelo menos, duas composições de Harrison. Suas músicas
para o grupo incluem "Taxman", "Within You Without You", "While My Guitar Gently Weeps", "Here Comes the Sun" e
"Something". Esta última se tornou a segunda música mais regravada dos Beatles, perdendo apenas para "Yesterday"."""

palavras = texto.split()

# print(palavras)
res = Counter(palavras)
print(res)

print(res.most_common(5)) # Encontrando as 5 palvras com mais ocorrencia no texto


"""
Módulo Collections - Default Dict
# Recap Dicionarios

dicionario = {'curso': 'Programação em Python'}
print(dicionario) Imprime tudo
print(dicionario['curso']) Imprime o valor
print(dicionario['outro']) # Key ERROR

Default Dict -> Ao criar um dicionario utilziando o Default dict, nós informamos um valor default,
podendo utilziar um labda para isso. Este valor sempre será utilizado sempre que não houver
um valor definido. Caso tentemos acesar uma chave que não existe, essa chave será criada
e o valor default será atribuído.

OBS: Lambdas são funçoes  sem nome, que podem ou não receber parâmetros de entrada
e retornar valor
"""

# Fazendo import
from collections import defaultdict
dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['curso'] = 'Programação Python'
print(dicionario)
print()
print(dicionario['outro'])  # Key error no dicionario comum, mas aqui nao
print(dicionario)

"""
Módulo Collections - Ordered Dict
# Em um dicionario a ordem de inserção de elementos não é garantida;

Ordered Dict -> é um dicionario que nos garante a ordem de inserção dos elementos.
"""

# Fazendo import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2,'c': 3,'d': 4, 'e': 5, 'f': 6})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""
Módulo Collections - Named Tuple

## Recap Tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas onde, especificamos um nome para a mesma e também
parâmetros.
"""
# IMportando

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1: Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2: Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3: Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='WHO')
print(ray)

# Acessando os dados
print(ray[0])  # idade
print(ray.raca)

"""
Módulo Collections - Deque


Deque -> Podemos dizer que o deque é uma lista de alta performance;

"""

# Importa

from collections import deque

# Criando

deq = deque('Wellington')
print(deq)

# Adicionando elementos

deq.append('X')  # Adiciona ao final
print(deq)

deq.appendleft('F') # Adiciona ao inicio
print(deq)

# Remover elementos

print(deq.pop())  # Remove e retorna o ultimo elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)


