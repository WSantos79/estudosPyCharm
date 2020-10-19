"""
Generators Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set(Conjunto) Comprehension;

Não vimos:
- Tuple Comprehension.... porque elas se chamam Generators
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))  # Verefica se todos começam com C, True

# Poderíamos ter feito utilizando Generators:

print(all(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generators
res1 = (nome[0] == 'C' for nome in nomes)
print(type(res1))

''' Generatos ocupa menos espaço e memoria do que qualquer outro Comprehension'''

# Prova disso:

from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set(conjunto) Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generetors
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generators Expression: {gen} bytes')

# Eu posso iterar no Generators Expression? sim

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

