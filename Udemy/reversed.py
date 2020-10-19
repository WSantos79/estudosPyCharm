"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iteravel.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto(Set)
print(set(reversed(lista)))  # Em conjuntos (SET), não definimos a ordem dos elementos

# Podemos iterar sobre o reversed
for letra in reversed('Wellington e Tarcia'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do For
print('\n')
print(''.join(list(reversed('Wellington e Tarcia'))))


# Já vimos como fazer isso mais fácil com  o slice de strings

print('Wellington e Tarcia'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso

for n in reversed(range(0, 10)):
    print(n)

# Apesar que já vimos como fazer isso utilizando o próprio range()
print('\n')
for n in range(9, -1, -1):
    print(n)

