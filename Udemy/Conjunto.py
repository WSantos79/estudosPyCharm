# Um conjunto (set) tem apenas valor
# Um mapa (dicionario) tem chave e valor
"""
Sets ( Conjuntos ) não possuem valores duplicados;
Sets ( Conjuntos ) não possuem valores ordenados;
Elementos não são acessados via índice, ou seja, conjuntos não são indexados;
"""

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Mesmo com valores repetidos, ele nao gera erro, mas ignora e nao imprime
print(s)
print(type(s))

s = {1, 2, 3, 4, 5, 5}  # Forma mais Comum de CRIAR
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')



lista = [99, 23, 23, 45, 56, 27, 74, 33, 65, 33]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99, 23, 23, 45, 56, 27, 74, 33, 65, 33)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 23, 23, 45, 56, 27, 74, 33, 65, 33], 'dict')
# Dicionario nao aceita Chaves duplicadas
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 23, 23, 45, 56, 27, 74, 33, 65, 33}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Podemos ITERAR em um Set normalmente:
for valor in conjunto:
    print(valor)

# adicionando elementos em conjuntos
print(conjunto)
conjunto.add(555)
print(conjunto)

# remover elementos
conjunto.remove(555)
print(conjunto)     # se o valor nao existir, gera erro

# forma 2 de remover elementos
conjunto.discard(74)
print(conjunto)     # se o valor nao existir, NAO gera erro

s = {1, 2, 3}
print(s)

# COPIANDO = Deep Copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Copiando = Shallow Copy

novo = s
novo.add(4)

print(novo)
print(s)

# remover todos os itens do conjunto
s.clear()
print(s)

""" metodos matematicos de conjuntos
Imagine que temos dois conjuntos um contendo os estudants de java
e outro de python
"""

estudante_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Vitor'}
estudante_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Precisamos gerar um conjunto com nomes unicos

# Forma 1 : Union
print(estudante_java)
print(estudante_python)
unicos1 = estudante_java.union(estudante_python)
print(unicos1)

# Forma 2 : caractere pipe | |

unicos2 = estudante_python | estudante_java
print(unicos2)

## Gerar um conjunto de estudantes que estao em ambos cursos

# Forma 1 : intersection
ambos1 = estudante_java.intersection(estudante_python)
print(ambos1)

# Forma 2 :  & & &

ambos2 = estudante_python & estudante_java
print(ambos2)

## Gerar estudantes de um curso que nao estao em outro

so_python = estudante_python.difference(estudante_java)
so_java = estudante_java.difference(estudante_python)
print(so_java)
print(so_python)

# Soma, maior, minimo, tamanho

s = {1, 2, 3, 5, 6, 77, 777, 34}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

