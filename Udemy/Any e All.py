"""
Any e All

all() -> Retorna True se todos os elementos do iteravel sao verdadeios ou ainda se o iteravel esta vazio.

"""

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # TOdos os números são verdadeiros? False, 0 é False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))  # Verefica se todos começam com C, True

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # se ele forem par
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))  # se eles forem impar


"""
any() -> Retorna true se qualquer elemento do iterável for verdadeiro. Se o iteravel estiver vazio, retorna False
"""

print(f'Any = {any([0, 1, 2, 3, 4])}')  # True



