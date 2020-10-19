"""
*args

- O *args é um parãmetro, como outro qualquer. Isso significa que você poderá chamar
de qualquer coisa, desde que começe com asterístico *.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo.

Mas o que é *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos:


def soma_todos_numeros(n1=0, n2=0, n3=0):
    return n1 + n2 + n3


print(soma_todos_numeros(4, 6, 5))
#  print(soma_todos_numeros(4, 6, 5, 5)) TypeERROR

"""

# Entendendo o *args
# Args não é obrigatorio informar


def soma_todos_elementos(*args):
    print(args)
    return sum(args)  # Por ser uma tupla podemos utilziar sum()
   # total = 0
   # for numero in args:
   # total = total + numero
   # return total


print(soma_todos_elementos(4, 6, 5))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(soma_todos_elementos(lista)) # TypeERROR

# é preciso desempacotar a lista para usar dentro da  tupla *args

# Desempacotador
print(soma_todos_elementos(*lista))  # OBS o * serve para que informemos ao python que estamos passando uma coleçao de
# dados dessa forma ele saberá que antes precisara desempacotar os dados

conjunto = {5, 5, 4, 7, 6, 3}  # nao se repete numero
print(soma_todos_elementos(*conjunto))


