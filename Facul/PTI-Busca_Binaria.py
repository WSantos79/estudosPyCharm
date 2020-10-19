def busca_binaria(vaca, buscar):
    minimo = 0
    maximo = len(vaca) - 1

    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if buscar < vaca[meio]:
            maximo = meio - 1
        elif buscar > vaca[meio]:
            minimo = meio + 1
        else:
            return meio
    return -1


vacas = list(range(1, 2000, 2))
print(vacas)

alvo = int(input("\nInforme a Vaca a ser buscada: "))
ordenhada = busca_binaria(vacas, alvo)

if ordenhada >= 0:
    print(f'\nA vaca {alvo} já foi ordenhada.')
else:
    print(f'\nA vaca {alvo} ainda não foi ordenhada.')


