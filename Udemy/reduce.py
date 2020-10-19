"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in).
Agora temos que importar e utilizar esta função a partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop´for é mais legível.

Para entender o Reduce:

# imaine que você tem uma coleção de dados:

dados = [a1, a2, a3]

# E voce tem uma função que recebe dois parâmetros

def funcao(x, y):
    return x * y

Assim como map() e filter() a função reduce() recebe dois parâmetros: a função e o iterável

reduce(funcao, dados)

A função reduce funciona da seguinte forma:
    Passo 1 : res1 = f(a1, a2) # aplica a funçao nos dois primeiros elementos da coleçao e guarda o resultado.
    Passo 2 : res2 = f (res1, a3) # aplica a funçao passando o resultado do passo 1 mais o terceiro o elemento e guarda
    o resultado

    Isso é repetido até o final.

    Passo 3: res3 = f(res2, a4)
    .....

    Ou seja, em cada passo ela aplica a funçao passando o primeiro argumento o resultado da aplicaçao anterior.
    no final, reduce() ira retornar o resultado final.

Alternativamente, poderiamos ver a funçao reduce() como :

funcao(funcao(a1, a2), a3), a4) ... ) an)
"""

# multiplicando todos elementos de uma lista

from functools import reduce

dados = [2, 3, 4,  5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o  reduce() nós precisamos de uma funçao que receba dois parametros

mult = lambda x, y: x * y
res = reduce(mult, dados)

print(res)

# Utilizando um loop normal

x = 1
for n in dados:
    x = x * n

print(x)


''' É preferivel utilizar o loop comum '''
