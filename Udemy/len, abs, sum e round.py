"""
Len, Abs, Sum e Round

# Len

len() - > Retorna o tamanho  ( ou seja, o número de itens) de um iterável.
"""

print(len('Wellington'))  # quantos caracteres

print(len([1, 2, 3, 4, 5]))  # quantidade de caracteres

# Por debaixo  dos panos quando utilizamos a função len() o Python faz o seguinte:

print('Wellington'.__len__())  # Dunder len

"""
ABS

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.
"""

# Retorna todos Positivos
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

"""
SUM

sum() -> Recebe como parâmetro um iterável, podendo receber um valor  inicial, e retorna a soma total dos elementos,
incluindo o valor inicial.

OBS: O valor inicial default = 0
"""

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([1, 2, 3, 4, 5], -5))

"""
Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal, Se a precisão
não for informada retorna o inteiro mais próximo da entrada;
"""
print('\n')
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121212121, 2))
print(round(1.21999992329, 2))
