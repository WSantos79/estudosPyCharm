"""texto = Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).

texto = texto.lower()
texto = texto.replace('(', '').replace(')', '').replace('.', '').replace(',', '')

lista_palavras = texto.split()



print(lista_palavras)

total = lista_palavras.count('string') + lista_palavras.count('strings')

print(total) """
import inline as inline
import matplotlib

"""
def extrair_lista_email(dict_1, dict_2):
    lista_1 = list(zip(dict_1['nome'], dict_1['email'], dict_1['enviado']))
    print(f"Amostra da lista 1 = {lista_1[0]}")

    lista_2 = list(zip(dict_2['nome'], dict_2['email'], dict_2['enviado']))

    dados = lista_1 + lista_2

    print(f"\nAmostra dos dados = \n{dados[:2]}\n\n")

    # Queremos uma lista com o email de quem ainda não recebeu o aviso
    emails = [item[1] for item in dados if not item[2]]

    return emails


dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker',
             'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org',
              'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu',
              'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com',
              'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis',
             'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com',
              'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net',
              'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}

emails = extrair_lista_email(dict_1=dados_1, dict_2=dados_2)
print(f"E-mails a serem enviados = \n {emails}")  


cpf = ['111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']


def procurar(onde, oque):   #  Busca linear
    tamanho = len(onde)
    for n in range(tamanho):
        if oque == onde[n]:
            return True

    return False

def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace('-', '').replace('.', '')
        if len(cpf) == 11:
            if not procurar(lista_dedup, cpf):
                lista_dedup.append(cpf)
    return lista_dedup


def testar_funcao(lista_cpf):
    lista_dedup = criar_lista_dedup(lista_cpf)
    print(lista_dedup)


testar_funcao(cpf)


 DESAFIO HACKER MISSING NUMBERS
 
 
from collections import Counter
n,arr=int(input()),list(map(int,input().split()))
m,brr=int(input()),list(map(int,input().split()))
a,b=Counter(arr),Counter(brr)
print(*(sorted((b-a).keys()))) 

--------------------------------------------------------------------------------------------------------------------

n = int(input("Digite a quantidade total de números existentes : "))
p = int(input("Digite o tamanho da combinação desejada: "))

total = 1



              n!
            p!(n - p)!




tt3 = n - p
total3 = 1
totalp = 1
totaln = 1
w = n - tt3


lista = []

for z in range(w):
    lista.append(n)
    n = n - 1

for x in range(p):
    totalp = totalp * (x + 1)

for x in lista:
    totaln = totaln * x

# print(f"A sua chance é de 1 em N {totaln}")
# print(f"A sua chance é de 1 em P {totalp}")  # 720
# print(lista)
final = totaln / totalp
print(f'\n{final}')




-----------------------------------------------------------------------------------------------------------------------

def busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True
    return False


def criar_lista_dedup(lista):
    lista_dedup = []
    for cpf in lista:
        cpf = str(cpf)
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) == 11:
            if not busca_binaria(lista_dedup, cpf):
                lista_dedup.append(cpf)
    return lista_dedup


def testar_funcao(cpf):
    lista_dedup = criar_lista_dedup(cpf)
    print(lista_dedup)


cpf = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22',
       '333.333.333-33', '22222222222', '444.44444']
cpf.sort()


testar_funcao(cpf)



def calcular():
    imposto = 27
    while imposto > 0:
        imposto = input("imposto ou s (sair)")
        if not imposto:
            imposto = 27
        elif imposto == 's':
            break
        else:
            imposto = float(imposto)
        print(f'Valor final {salario - (salario * (imposto / 100))}')


salario = int(input("Salario : "))


calcular()



def fib(n):
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado


print(fib(5))


x = [1, 2, 3]
y = _a
x.append(4)
print(y)
"""


def busca_binaria(v, p, r, x):
    # condição de parada

    if p <= r:

        q = (p + r) // 2  # buscando o índice do meio do vetor
        if x > v[q]:
            return busca_binaria(v, q + 1, r, x)
        elif x < v[q]:
            return busca_binaria(v, p, q - 1, x)
        else:
            return q  # encontrado
    return -1  # não encontrado


vacas_ordenhadas = list(range(1, 5000))

vaca = 5001

posicao = busca_binaria(vacas_ordenhadas, 0, len(vacas_ordenhadas) - 1, vaca)

if posicao >= 0:

    print("A vaca %d foi ordenhada e se encontra na posição: %d." % (vaca, posicao))

else:

    print("A vaca NÃO foi ordenhada.")

print(vacas_ordenhadas)
