
import sqlite3


conn = sqlite3.connect('aulaDB.db')
"""  
print(type(conn))

ddl_create = '''
create table if not exists fornecedor (
    id_fornecedor integer not null primary key autoincrement,
    nome_fornecedor text not null,
    cnpj varchar(18) not null,
    cidade text,
    estado varchar(2) not null,
    cep varchar(9) not null,
    data_cadastro date not null
    );
'''
print("\n")
cursor = conn.cursor()
cursor.execute(ddl_create)
print(type(cursor))

print("Tabela criada!")
print(f"Descrição do cursor: {cursor.description}")
print(f"linhas afetadas: {cursor.rowcount}")
cursor.close()
conn.close()


conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute('''
insert into fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
values ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
''')

cursor.execute('''
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
''')

cursor.execute('''
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
''')

conn.commit()

print('\n')

print(type(cursor))

print("Tabela criada!")
print(f"Descrição do cursor: {cursor.description}")
print(f"linhas afetadas: {cursor.rowcount}")


cursor.close()
conn.close()

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),
    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),
    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
]

cursor.executemany('''
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES (?, ?, ?, ?, ?, ?)''', dados)

conn.commit()

print('\n')
print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
print('\n')
for linha in resultado:
    print(linha)



print('\n')
cursor.execute("SELECT * FROM fornecedor WHERE id_fornecedor = 5")
resultado = cursor.fetchall()
print(resultado)

print('\n')
conn.commit()
"""


cursor = conn.cursor()


# Lista as tabelas do banco de dados
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")
print('Tabelas:')
for tabela in cursor.fetchall():
    print(tabela)

# Captura a DDL usada para criar a tabela
tabela = 'fornecedor'
cursor.execute(f"""SELECT sql FROM sqlite_master WHERE type='table' AND name='{tabela}'""")
print(f'\nDDL da tabela {tabela}:')
for schema in cursor.fetchall():
    print("%s" % schema)


cursor.execute("SELECT * FROM fornecedor")

# print(cursor.fetchall())


for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()

