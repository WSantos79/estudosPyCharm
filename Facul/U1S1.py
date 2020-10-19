'''def calculo(a):
    r = 200 * a
    return r


mes = int(input("Digite o mês que deseja saber o resultado "))
# mes = int(mes)
print(f'A previsão para o mês {mes} é de {(calculo(mes))} vendas')

-----------------------------
a = 2
b = 0.5
c = 1


x = float(input('Digite o valor de X: '))


print(f'o Valor de y para x = {x} é {a * x ** 2 + b * x + c}')




'''

salario = int(input("Salario: "))

ir = input("Imposto: ")

if not ir:
    ir = 27.5
else:
    ir = float(ir)

sal = salario - (salario * (ir / 100))

print(sal)