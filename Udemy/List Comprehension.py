"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]
"""

# Exemplois

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [lista * 10 for lista in lista]

print(res)

# List Compreehsion

print([lista * 2 for lista in lista])

# Outros Exemplos

# 1

nome = 'wellington e tarcia'

print([nome.upper() for nome in nome])

# 2

lista_amigos = ['maria', 'julia', 'pedro', 'rodrigo', 'vanessa']

print([lista_amigos.title() for lista_amigos in lista_amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

"""
Nós podemos adicionar estruturas condicionais lógicas às nossas List Compreehnsion
"""

numero = [1, 2, 3, 4, 5, 6]  # Lista

pares = [numero for numero in numero if numero % 2 == 0]

impar = [numero for numero in numero if numero % 2 != 0]

print()
print(f'Pares = {[numero for numero in numero if numero % 2 == 0]}')
print(f'Ímpares = {[numero for numero in numero if numero % 2 != 0]}')

# Refatorar
print()
# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
print(f'Pares = {[numero for numero in numero if not numero % 2]}')
# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
print(f'Ímpares = {[numero for numero in numero if numero % 2]}')

"""
Dictionary Comprehension

lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
conjuntoSET = {1, 2, 3, 4}  
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Sintaxe 
{chave:valor for valor in ireravel}

se fosse lista = [valor for valor in iteravel]
"""

# Exemplo


dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print()
quadrado = {chave:valor ** 2 for chave, valor in dicionario.items()}

print(quadrado)


