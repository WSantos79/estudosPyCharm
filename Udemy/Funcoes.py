"""
Definindo funções

 Em Python, a gorma geral de definir uma função é:

 def nome_da_funcao(parametros_de_entrdda):
     bloco_da_funcao

Onde:
nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snack Case)

parametros_de_entrada -> são opcionais, onde tendo mais de um, cada um separado por virgula, podendendo ser
opcionais ou não;

bloco_da_funcao -> também chamado de corpo da funçao ou implmentaçao, é onde o processando da funcao acontece,
nesse bloco pode ter ou não retorno da função;

OBS: Veja que para definir uma funçao, utilizamos a palavra reservada 'def' informando ao Python
que estamos definindo uma funçao. Tabmém abrimos o bloco de codigo com dois pontos :
"""
# Definindo funções

def diz_oi():
    print('oi')

"""
OBS: 
1- Veja que, dentro das nossas funções podemos utilizar outras funções;
2- Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3- Veja que esta função não recebe nenhum parâmetro de entrada;
#####  4- Veja que esta função não retorna nada; ####
"""

# Utilizando Funções
# Chamada de execução
diz_oi()

"""
Funções com retorno ########

"""

# Exemplo funçao com retorno


def quadrado():  # quadrado de 7
    return 7 * 7


print(f'Retorno: {quadrado()}')
print()


def diz_cu():
    print('Estou ANTES do return...')
    return 'Digo cu'
    print('Estou depois do return, e nunca vou ser executado...')


print(diz_cu())


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


def outra_funcao():
    return 2, 3, 4, 5  # è uma tupla


print(f'Retorna Tupla {outra_funcao()}')


# Funçao cara ou coroa, jogar moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print()
print(joga_moeda())


"""
Funções com Parâmetros (de entrada)

- Funções que recebem dados para semrem processados dentro do mesmo;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;
"""

# Refatorando função


def quadrado(n):
    # return n * n
    return n ** 3  # N elevado ao quadrado ( ** ) = elevado a 2 ( quadrado )  ou a 3 ( ao cubo )
    # ( ** ) exponencial


print(quadrado(2))
print(quadrado(5))
print(quadrado(7))

print()


def cantar_parabens(aniversariante):
    print('Parabéns para  você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a/o {aniversariante}!!')


cantar_parabens('Tarcia')


def soma(a, b):
    return a * b


print(soma(5, 3))
print()


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:  # Se o número for ímpar ( se o numero nódulo por 2 for diferente de 0)
            total = total + 1
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(f'O total de ímpares é {soma_impares(lista)}')

"""
Funções com parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional:
print('Tarcia')
print()
"""


def exponencial(numero, potencia=2):  # Se eu informar o valor ele se torna opcional
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3     = 9
print()
print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva á potencia informada pelo usuário

# OBS : Em funções Python, os parâmetros com valores default DEVEM SEMPRE estar ao final da declaração;

#ERRO!
'''
#ERRO!

def teste(num=2, potencia):
    return num ** potencia


print(teste())

'''


def teste(num=2, potencia=0):
    return num ** potencia


print(teste(2, 3))

# Exemplo com default de função
def soma  (n1, n2):
    return n1 + n2


def mat(n1, n2, fun=soma):
    return fun(n1, n2)


def subtracao(n1, n2):
    return n1 - n2


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Evite variável global sempre que possa !!!!
# Utilizando variavel global dentro de funçao

total = 0


def incrementa():
    global total
    total = total + 1
    return total


print()
print(incrementa())  # = 1
print(incrementa())  # = 2
print(incrementa())  # = 3


# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # ta dizendo q é uma variavel local
        contador = contador + 1
        return contador
    return dentro()


print(f'\nFunção fora = {fora()}')  # SEMPRE VAI DAR 1
print(f'\nFunção fora = {fora()}')  # SEMPRE VAI DAR 1
print(f'\nFunção fora = {fora()}')  # SEMPRE VAI DAR 1

""" 
Docstrings

"""

def diz_oi():
    """Uma função simples que retorna 'oi'"""
    return 'oi'

'''

## acessar docstrings,
## digitar no terminar  python
## from Funcoes import diz_oi
##  print(diz_oi.__doc__)


# Ou help(diz_oi)
'''