"""
utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.

"""

# Função em Python

def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão em Lambda

lambda x: 3 * x + 1

# E como utilizar a expressão lambda??
calc = lambda x: 3 * x + 1   # Não é uma forma digna de utilização

print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

# strip remove espaço de inicio e fim de uma string, espaços

print(nome_completo('  tarcia', 'mara   '))


amar = lambda: 'Como não amar a Tarcia?'

print(amar())

# Outro exemplo:

autores_lista = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert',
                 'Orson Scott Card', 'Douglas Admas', 'H. G. Wells', 'Leigh Brackett']

print()
print(autores_lista)

autores_lista.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
# -1 pega o ultimo nome, lower para deixar tudo igual, sort pra colocar em ordem alfabetica? split para transfomar
# cada uma das palavras em uma separada
print(autores_lista)


# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """retorna a funçao = f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))  # passando o valor do x
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))

