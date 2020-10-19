"""
Módulo Randon

- Em Python, módulos nada mais são do que outros arquivos Python.


"""

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1: Importando todo o módulo (Não recomendado)

import random

# Ao realizar o importo de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (ficaram em memória)

# randon() -> Gera um número REAL pseudo-aleatório entre 0 e 1

print(random.random())  # nome da funçao ponto nome do pacorte.... funçao random, pacote random

""" Forma 2 - Importando uma função especifica do módulo '''Forma Recomendada"""

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() -> gerar um número  REAL pseudo-aleatório entre os valores estabelecidos

from random import uniform

print(uniform(0, 20))

print('\n')

for i in range(10):
    print(uniform(3, 7)) #  7 nao é incluido


# randint()  -> Gera um número INTEIRO pseudo-aleatórios entre os valores estabelecidos

# Gerador de apostas para mega-sena
print('\n')
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1 e vai ate 60

# choice() -> mostra um valor aleatório entre um iterável

jogadas = ['pedra', 'papel', 'tesoura']
print('\n')
from random import choice

print(choice(jogadas))

# shuffle() -> tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', '1', '2', '3', '4', '5', ' 6', '7']

print(cartas)

shuffle(cartas)

print(cartas)