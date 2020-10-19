"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só funciona
em listas.

Podemos utilziar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted() sempre retorna uma lista com os elementos do iteravel ordenados
"""

lista = [4, 56, 7, 1, 712, 7, 0, 5]
tupla = (4, 56, 7, 1, 712, 7, 0, 5)

print(lista)
print(sorted(lista))  # Ordenar do menor para o maior

print(lista)

# Adicionando parâmetros ao sorted()

print(sorted(lista, reverse=True))  # Ordena do maior para o menor

# podemos converter para outro tipo

print(tuple(sorted(lista)))

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# ordenar pelo tamanho do dicionario

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario["username"]))  # ordem alfabetica do nome

print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))  # Ordenando pel onumero de tweets

print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True))

# ultimo exemplo

musicas = [
    {"titulo": "ThunderStruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

print(sorted(musicas, key=lambda tocou: (tocou["tocou"])))  # ordena da menos tocada para mais tocada

print(sorted(musicas, key=lambda tocou: (tocou["tocou"]), reverse=True))
