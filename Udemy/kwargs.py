"""
**kwargs

- O **kwargs é um parâmetro, como outro qualquer. Isso significa que você poderá chamar
de qualquer coisa, desde que começe com asterístico **.

Exemplo:

**xis

Mas por convenção, utilizamos **kwargs para defini-lo.

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em
uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.

# Nas nossas funções podemos ter (NESTA ORDEM)

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs

"""

# Exemplo:


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():  # iterando dicionarios com .items
        print(f'A cor favorita de {pessoa.title()} é {cor.title()}')  # Utilizando .title() para deixar a primeira
        # letra maiuscula


cores_favoritas(marcos='verde', wellington='preto', tarcia='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios;


def cumprimento_especial(**kwargs):
    # chave geeks, valor python
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return "Você recebeu um cumprimento Pythônico Geek!"
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é ...'


print()
print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))
print(cumprimento_especial(wellington='Tarcia'))
'''
# Nas nossas funções podemos ter (NESTA ORDEM)

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs
'''


def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(f'args = {args}')
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(f'kwargs = {kwargs}')


print()
minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=False)
minha_funcao(34, 'Felipe', eu='Nao', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Desempacotando com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Wellington', 'sobrenome': 'Santos'}
print()
print(mostra_nomes(**nomes))


def soma(a, b, c):
    return a + b + c


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

print()
print(f"Soma = {soma(1, 2, 3)}")
print(f"Lista = {soma(*lista)}")
print(f"Tupla = {soma(*tupla)}")
print(f"Conjunto = {soma(*conjunto)}")
print(f"Dicionario = {soma(**dicionario)}")  # Quando for dicionario é DUPLO ASTERISTICO **

# OBS > Os nomes da chave no dicionário devem ser o mesmo dos parâmetros da função










