"""
Filter

filter() - > filtrar dados de uma determinada coleção.
"""

import statistics

# dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a funçao mean()

media = statistics.mean(dados)
print(media)
'''OBS > assim como a funçao map(), a filter() recebe dois parametros,
sendo uma funçao e um iteravel'''


# filtrando todos os dados que sao maiores que a media
res = filter(lambda x: x > media, dados)

print(list(res))

# OBS: assim como map depois de utilizar os dados, eles são excluídos da memoria

paises = ['', 'Argentina', '', 'Brasil', 'Cuba', 'Venezuela', '', 'Colombia', '']

print(paises)

# Retirando os espaços em brancos
res = filter(None, paises)

print(list(res))

'''
A diferença entre map e filter

map() -> recebe dois parametros, uma funçao e um iteravel e retorna um objeto mapeando a funçao para cada elemento 
do iteravel.

filter() -> recebe dois parametros, uma funçao e um iteravel e retorna um objeto filtrando apenas os elementos 
de acordo com a funçao.

'''

# exemplo mais complexo

# uma lista com dicionarios dentro
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)

# Filtar os usuarios que estao inativos no Twitter

# Forma 1
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

print(inativos)

# Forma 2

ina = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(ina)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo "sua instrutora é" + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)



