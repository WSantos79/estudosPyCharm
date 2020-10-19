"""

open() -> Na forma mais simples  de utilização nós passamos apenas um parâmetro de entrada,
que neste caso é o nome do arquivo a ser lido. Essa função retorna um _io.textIOWrapper e é com ele
que trabalhamos então
"""

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo)  # <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# modo = r.... r ->  read
print(type(arquivo))

print('\n')

print(arquivo.read())
print(arquivo.read())  # nao acontece nada
# o python utiliza um recurso para trabalhar com arquivos chamado cursos. Esse cursor, funciona como o
# cursor quando estamos escrevendo.
# OBS: a função read() lê todo o conteúdo do arquivo.

