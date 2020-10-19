"""
Seek e Cursors

seek() -> é utilizado para movimentar o cursor pelo arquivo.


OBS: Sempre ao abrir um arquivo, feche o arquivo .close()
arquivo.close()


"""

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

#  Movimento o  cursor pelo arquivo com a função seek()
print('\n----------------------------------------------------------------------------------------------')

arquivo.seek(115)


print(arquivo.read())

print('\n----------------------------------------------------------------------------------------------')

# readline() -> função q ue lê o arquivo linha a linha
arquivo = open('texto.txt', encoding='utf-8')
print(arquivo.readline())
print(arquivo.readline())

print('\n----------------------------------------------------------------------------------------------')

arquivo = open('texto.txt', encoding='utf-8')
ret = arquivo.readline()
print(ret)
print(type(ret))
print(ret.split(' '))

print(arquivo.closed)

arquivo.close()
print(arquivo.closed)
