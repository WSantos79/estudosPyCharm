"""
INTRODUÇÃO A MANIPULAÇÃO DE DADOS EM PANDAS



import pandas as pd


print([pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()])
print('\n\n')
print([pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head()])
print('\n\n')
"""
# Manipulação de dados com pandas
import pandas as pd
df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

# print(df_selic.info())
df_selic.drop_duplicates(keep='last', inplace=True)  # Remover linhas duplicadas
# Caso inplace não seja passado, a transformação é aplicada, mas não é salva, ou seja,
# o DF continua da mesma forma anterior a transformação
# pedindo para manter o último registro (keep='last')

'Criar novas colunas'

# criar coluna com data de extração e coluna com o nome do responsavel

from datetime import (
    datetime as dt,
    date)

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autora"

print(df_selic.info())
print('\n')
print(df_selic.head())

# Método to_datetime() e astype()   ==== data do panda, para manipular melhor

df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
df_selic['data_extracao'] = df_selic['data_extracao'].astype('datetime64[ns]')

print(df_selic.info())
print('\n')
print(df_selic.head())

# Series.str

#df_selic['responsavel'] = df_selic['responsavel'].str.upper()
#print(df_selic.head())


# Método sort_values()  = que permite ordenar o DF

df_selic.sort_values(by='data', ascending=False, inplace=True)
# ascending = ordem crescente ou decrescnte.... inplace = sobrescrever o df

# Método reset_index() e set_index()
df_selic.reset_index(drop=True, inplace=True)  # reseta os index que foram modificados ao ordernar pela data
#print(df_selic.head())

lista = [f'selic_{indice}' for indice in df_selic.index]
df_selic.set_index(keys=[lista], inplace=True)
print(df_selic.head())


# Etapa de extração de informações
# Filtros com loc

df_selic.loc['selic_0']  # Retorna os dados da selic_0

df_janeiro


