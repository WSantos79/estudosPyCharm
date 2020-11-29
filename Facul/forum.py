
lista = [1, 2, 3, 4, 5, 6, 7]


lista.append(12)
lista.pop()

for numero in lista:
    if numero % 2 == 0:
        print(f'Número par: {numero}')
    else:
        print(f'Número ímpar: {numero}')
