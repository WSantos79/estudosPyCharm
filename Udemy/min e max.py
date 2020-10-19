"""
Min e Max

max() - > Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.
"""

lista = [1, 2, 6, 130, 31, 12, 5, 22, 21]

print(max(lista))  # Retorna 130

# faça um programa que receba dois valores do usuario e mostre o maior

#valor1 = int(input('Informe o primeiro valor: '))
#valor2 = int(input('Informa o segundo valor: '))

#rint(f'O maior valor é {max(valor1, valor2)}')

"""
Min

min() - >  Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.
"""

ista = [1, 2, 6, 130, 31, 12, 5, 22, 21]

print(min(lista))  # Retorna 130

# faça um programa que receba dois valores do usuario e mostre o maior

#valor1 = int(input('Informe o primeiro valor: '))
#valor2 = int(input('Informa o segundo valor: '))

#print(f'O menor valor é {min(valor1, valor2)}')


# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Oliver Queen']

print(max(nomes))  # Considera ordem alfabetica
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome))) # Ordena pelo tamanho do nome

musicas = [
    {"titulo": "ThunderStruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

#  print(max(musicas))  # nao funciona

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO Imprima somente o titulo da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO como encontrar a musica mais tocada e menos tocada, sem usar o max/min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

