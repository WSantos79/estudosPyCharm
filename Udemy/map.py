"""
Map

Com map, fazemos mapeamento de valores para função.
"""

import math


def area(r):
    """Calcula a area de um circulo com raio 'r' """
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

# mas se eu tivesse uma lista com varios raios
raios_lista = [2, 5, 8, 4.5, 10, 44, 0.3]

# Forma comum

areas = []
for r in raios_lista:
    areas.append(area(r))


print(areas)

# Forma com map
# map é uma funçao que recebe dois parametros: o primeiro a funçao, a segunda o iteravel
areas = map(area, raios_lista)
print(list(areas))  # ou print(tuple(areas))

# ---------------------------------------------------------
print()
print(areas)  # retorna um map object
print(type(areas))  # type map


'''
map mapea os dados, pega os dados e raio lista e passa para dentro da funçao area
'''

# Forma map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios_lista)))


""" OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera."""


# Para fixar - Map

# Temos dados iteráveis

# dados: a1, a2 .... an

# temos uma funçao:

# funçao: f(x)

# utilizamos a funçao map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplica a funçao.

# O map object: f(a'), f(a2), f(....),

'''Mais um exemplo'''

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19)]
# lista contendo tuplas
print(cidades)

# conversao de gral celcios para farenight

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)


print(list(map(c_para_f, cidades)))

