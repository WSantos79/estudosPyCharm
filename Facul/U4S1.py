import pandas as pd

'''
lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

series_dados = pd.Series(lista_nomes)



print(series_dados.loc[3])

-------------------------------------------------------------------------------------------------------------------

series_dados2 = pd.Series([10.2, -1, None, 15, 23.4])

print('Quantidade de linhas = ', series_dados2.shape)  # Retorna uma tupla com o número de linhas
print('Tipo de dados', series_dados2.dtypes)  # Retorna o tipo de dados, se for misto será object
print('Os valores são únicos?', series_dados2.is_unique)  # Verifica se os valores são únicos (sem duplicações)
print('Existem valores nulos?', series_dados2.hasnans)  # Verifica se existem valores nulos
print('Quantos valores existem?', series_dados2.count())  # Conta quantas valores existem (excluí os nulos)

print('Qual o menor valor?', series_dados2.min())  # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados2.max())  # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética?', series_dados2.mean())  # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão?', series_dados2.std())  # Extrai o desvio padrão de uma Series numérica
print('Qual a mediana?', series_dados2.median())  # Extrai a mediana de uma Series numérica

print('\nResumo:\n', series_dados2.describe())  # Exibe um resumo sobre os dados na Series

'''

# Construtor DataFrame com lista

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org' \
               ' non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails))  # cria uma lista de tuplas

print(f'Lista de tuplas: {dados}')

frame = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])
print(f'\nData Frame com lista: ')
print(f'{frame}')

dados2 = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs': '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'idades': [32, 22, 25, 29, 38],
    'emails': 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org'
              ' non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
}

frame2 = pd.DataFrame(dados2)
print(f'\nData Frame com dicionario: ')
print(f'{frame2}')

# Extraindo informações de um DataFrame

print('\nInformações do DataFrame Dicionario:\n')
print(frame2.info())  # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', frame2.shape)  # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', frame2.dtypes)  # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', frame2.min())  # Extrai o menor de cada coluna
print('\nQual o maior valor?\n', frame2.max())  # Extrai o valor máximo e cada coluna
print('\nQual a média aritmética?\n', frame2.mean())  # Extrai a média aritmética de cada coluna numérica
print('\nQual o desvio padrão?\n', frame2.std())  # Extrai o desvio padrão de cada coluna numérica
print('\nQual a mediana?\n', frame2.median())   # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', frame2.describe())  # Exibe um resumo

frame2.head()  # Exibe os 5 primeiros registros do DataFrame

'''#####  Seleção de colunas em um DataFrame'''
print('\n')
# frame2.nomes
coluna_nomes = frame2['nomes']

print(coluna_nomes)

coluna_idade = frame2.idades
print('\n')

print(coluna_idade)
print('\n')

print(f'Média de idades = {coluna_idade.mean()}')

print('\n')


colunas = ['nomes', 'cpfs']
duas_colunas = frame2[colunas]

print(duas_colunas)

#  raspagem web (web scraping)
print('\n\n\n')

import requests


texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
print(texto_string[:100])

# Obs: para saber qual tag buscar, antes é preciso examinar o código fonte da página que se deseja "raspar".

from bs4 import BeautifulSoup

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('span', attrs={'class': 'short-desc'})
print(type(bsp_texto))
print(type(lista_noticias))
print(lista_noticias[5])


x = lista_noticias[5].contents  # veja que contents, retorna uma lista do conteúdo
print(f'X = {x}')

dados = []
# Apendamos a nossa lista de dados uma tupla com as quatro informações que extraímos.
for noticia in lista_noticias:
    data = noticia.contents[0].text.strip() + ', 2017' # Dessa informação <strong>Jan. 25 </strong> vai extrair Jan. 25, 2017
    comentario = noticia.contents[1].strip().replace("“", '').replace("”", '')
    explicacao = noticia.contents[2].text.strip().replace("(", '').replace(")", '')
    url = noticia.find('a')['href']
    dados.append((data, comentario, explicacao, url))

x2 = dados[1]

print(f'\nx2 = {x2}')

# Agora que temos nossa lista de tuplas com os dados, podemos criar o DataFrame
# e disponibilizar para um cientista de dados fazer a análise de sentimentos

df_noticias = pd.DataFrame(dados, columns=['data', 'comentário', 'explicação', 'url'])

# df_noticias ... onde df = data frame

print(df_noticias.shape)
print(df_noticias.dtypes)
df_noticias.head()

print('\n\n\n')
print(df_noticias)
print('\n\n\n')
# pd.read_html()

'''url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))



url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))
'''

