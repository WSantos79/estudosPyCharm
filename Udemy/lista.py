'''nome = input("Qual seu nome?")

print(f'Seja bem-vindo {nome}')

idade = input(f'Qual a sua idade {nome.title()}')

print(f'A {nome} tem {idade} anos')

n = 'a'
if n in lista5:
    print(f'Encontrei {n}')
else:
    print(f'nao encontrei {n}')

'''

lista1 = [1, 99, 4, 15, 61, 87, 5, 7, 5, 8, 1]

lista2 = ['a', 'q', 'd', 'j', 'k', 'ld', 5]

lista3 = []

lista4 = list(range(11))

lista5 = list('Tarcia e Wellington')

'''lista1.sort()
print(lista1.count(1))
print(lista5.count('e'))

lista5.extend(' muito amor')

print(lista5.count('e'))

print(len(lista5))
lista5.pop()
print(len(lista5))

cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):
    print(indice, cor)

print(cores.index("branco"))
print(n.index(4)) '''

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 25]

# slices [inicio:FIM:passo]

print(n[:15:2])

print(max(n))
print(min(n))
print(sum(n))
print(len(n))

"""
Listas Aninhadas (Multidimensionais) ( Nested Lists)

- Alguns linguagens de programação possuem uma estrutra de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);
    
Em Python temos as Listas


"""

# Exemplos

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(lista)
print(type(lista))

# Como acessar os dados?
# Linhas e colunas [] []

print(lista[0])    # 1,2,3
print(lista[0][1])    # 2
print(lista[2][1])    # 8
print()
# Iterando com loops em uma lista aninhada

'''for lista in lista:
    for num in lista:
        print(num)
'''
# List Comprehension
print()
[[print(valor) for valor in lista] for lista in lista]


# Exemplo - Gerando um tabuleiro/matrix 3x3
print()
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]  # o primeiro gerou as linhas e o 2 as colunas
print(tabuleiro)

# Gerando jogadas para jogo da velha

print([['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)])


# Gerando valores iniciais

print([['*' for i in range(1, 4)] for numero in range(1, 4)])



# List reverse()

lista0 = [1, 2, 3, 4, 5, 6, 10, 11, 12]

print()
print(lista0)
#print(f'Lista reverse() = {lista0.reverse()}')
lista0.reverse()
print(f'Lista com reverse() {lista0}')

'''A função reverse() só funciona em listas.'''

