"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.

"""

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))


# Sempre podemos gerar uma lista, tupla ou set(conjuntos) ou dicionários
print('\n')
print(f'Lista = {list(zip1)}')
zip1 = zip(lista1, lista2)  #'Assim q é usado ele some da memoria.... tendo que re- executar para ter novamente'
print(f'Tupla =  {tuple(zip1)}')
print(f'Set(Conjunto) = {set(zip1)}')
print(f'Dicionário = {dict(zip1)}')

"""ELE Pega e faz pares, 1 elemento da lsita1 com o 1 elemento da lista2, 2 elemento da lista1 com o 2 elemento da lista2"""

lista3 = [10, 11, 12, 13, 14, 15, 17]
lista4 = [21, 22, 23, 24]

zip2 = zip(lista1, lista2, lista3, lista4)

print(f'Zip com 4 lista, sendo uma maior: {list(zip2)}')  # nao imprime os  que nao fazem pares

"""OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver 
trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elemtnso do menor 
iterável acabar."""

# Podemos utilizar diferentes iteráveis com o zip

lista = [1, 2, 3, 4, 5]
tupla = 6, 7, 8, 9, 10
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
conjunto = {16, 17, 18, 19, 20}  # Set

zip3 = zip(lista, tupla, dicionario.values(), conjunto)
print('\n')
print(f'Zip3 = {list(zip3)}')


# Lista de tuplas

dados = [(1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

print(list(zip(lista, tupla)))  # saporra  sem fazer o outro comendo, so imprimindo direto

# mais exemplos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
# posição 0 é a chave, vai ser o nome
# e vai pegar o max, do dado1, e dado2

# gerar um dicionario com a maior nota de cada estudante

print(final)

# Podemos utilziar o map() para fazer isso

final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final2))

# Se colocar cada parte no terminal fica mais facil pra entender, ver aula
