tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tupla1)

tupla2 = tuple(range(21, 41, 2))
# RANGE [inicio,FIM,passo]
print(tupla2)


print(max(tupla2))

print(23 in tupla2)

for a in tupla2:
    print(a)

print(len(tupla2))
print(tupla2.count(23))


## Devemos utilizar tuplas SEMPRE que nao precisarmos modificar os dados em uma coleçao

## Exemplos... meses,
## tuplas sao mais rapidas do que listas.
# tuplas deixam seu codigo mais seguro, pois sao imutaveis
#
print(tupla2[2])

tupla0 = 4,
tupla01 = 4, 2, 1

i = 0

while i < len(tupla1):

    print(tupla1[i])
    i = i + 1

nova = tupla1  # na tupla nao gera o problema shallaow copy, somente na lista se copia diferente

print(nova)

outras = (000, 101, 400, 100, 200, 300)

nova = nova + outras

print(nova)

for n in nova:
    print(n)
    