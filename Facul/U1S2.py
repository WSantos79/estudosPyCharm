texto = """A inserção de comentários no código do programa é uma prática normal. Em função disso, 
toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.
 O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do
  algoritmo implementado (BANIN, 2018, p. 45)."""


'''
a = 0
e = 0

for p, v in enumerate(texto):

    if v == 'a':
        print(f"Encontramos a letra 'a' na posição {p}")
        a = a + 1

    if v == 'e':
        print(f"Encontramos a letra 'e' na posição {p}")
        e = e + 1


print(f"Foram encontrado {a} vogais 'a' e {e} vogais 'e'")
'''

"""DESAFIO"""

salario = float(input('Informe o salário do colaborador: '))

if salario <= 1903.98:
    print('Você não paga IR')

elif 1903.98 < salario <= 2826.65:
    print(f'Você paga o IR de 7.5%, ficando com {salario - (salario * 0.075)}')

elif 2826.65 < salario <= 3751.05:
    print(f'Você paga o IR de 15%, ficando com {salario * (salario * 0.15)}')

elif 3751.05 < salario <= 4664.68:
    print(f'Você paga o IR de 22.5%, ficando com {salario * (salario * 0.225)}')

else:
    print(f'Você paga o IR de 27.5%, ficando com {salario * (salario * 0.275)}')

