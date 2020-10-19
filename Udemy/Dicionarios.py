# em algumas linguagens de programaçao os dicionarios sao conhecidos  como mapas
# pois sao coleçoes do tipo chave/valor

# dicionarios sao representados por chave {}

# CHAVE E VALOR SAO SEPARADOS POR DOIS PONTOS 'CHAVES:VALOR'

# NAO PODEMOS ter CHAVES REPETIDAS

###### Dicionario = {'chave1': 'Valor1', 'chave2': 'valor2', 'chave3': 'valor3'}


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

print(paises['br'])

print(paises.get('br'))  # FORMA RECOMENDADA DE ACESSAR

print('eua' in paises)  # Retorna True
print('Estados Unidos' in paises)  # Retorno False

localidades = {
    (35.6989, 95.2809): 'Escritorio em Tóquio',
    (12.6989, 95.2809): 'Escritorio em Nova York',  # tupla como chave, pois tuplas sao imutaveis
    (13.6989, 95.2809): 'Escritorio em São Paulo'
}

print(localidades)

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

receita['abr'] = 350  # mais comum de adcionar dados
print(receita)

novo_dado = {'maio': 500}

receita.update(novo_dado)

print(receita)

receita['maio'] = 555  # atualizaçao mais comum

print(receita)

receita.update({'maio': 666})

print(receita)

receita.pop('mar')  # RETIRANDO DADO, mais comum

print(receita)

retorna = receita.pop('maio')
print(retorna)

print(receita)

del receita['fev']  # RETIRANDO DADO, varios caso voce ve, mas neste caso o valor removido NAO é retornado

print(receita)

# Onde usar dicionarios??
#  Imagine que  voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de compras:
   Produto 1:
        -nome;
        -quantidade;
        -preço;
   Produto 2:
        -nome;
        -quantidade;
        -preço;
"""
# opçoes

# Opção 1 - poderiamos utilizar lista para isto ? sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['Syphon Filter 3', 1, 250.00]

carrinho.append(produto1)
carrinho.append(produto2)
print()
print(carrinho, 'lista')

#  Teriamos que saber qual o indice de cada informação no produto

# opção 2 - Poderiamos utilizar uma tupla pra isso ? sim

produto1 = ('Platstation 4', 1, 2300.00)
produto2 = ('Syphon Filter 3', 1, 250.00)

carrinho = (produto1, produto2)

print(carrinho, 'tupla')

#  Teriamos que saber qual o indice de cada informação no produto

# Opçao 3 - Poderiamos utilizar um dicionario para isto ? sim
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'Syphon Filter 3', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho, 'Dicionario')

# Desta forma facilmente removemos ou adcionamos produtos no carrinho
# e em cada produto podemos ter certeza de cada informação

dicionario = {'chave1': 'Valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

print('\n', dicionario)

# limpar o dicionario

dicionario.clear()
print(dicionario)

# Copiando um para outro

dicionario = {'chave1': 'Valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
# DEEP COPY ------------- CORRETO COPIA
novo = dicionario.copy()

print(novo)

novo['d'] = 4

print(novo, 'novo')
print(dicionario, 'dicionario')

# Shallow copy

novo2 = dicionario

print('\n', novo2, 'novo2')
novo2['x'] = 44
print(novo2, 'novo2')
print(dicionario, 'dicionario')

#### Forma nao usual de criar dicionario

outro = {}.fromkeys('a', 'b')
print('\n', outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

veja = {}.fromkeys('chave', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'valor')
print(veja)

for chave in veja:
    print(chave, 'fore')

for chave in veja:
    print(veja[chave])

receita = {'jan': 100, 'fev': 120, 'mar': 300}

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

print(receita.keys())

for chave in receita.keys():    # Modo pythonico
    print(receita[chave])

print(receita.values())

print(sum(receita.values())) # Soma dos valores
print(max(receita.values()))
print(min(receita.values()))
print(len(receita)) # contador

