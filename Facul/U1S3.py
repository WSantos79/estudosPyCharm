"""
1 - Parâmetro posicional, obrigatório, sem valor default (padrão).
2 - Parâmetro posicional, obrigatório, com valor default (padrão).
3 - Parâmetro nominal, obrigatório, sem valor default (padrão).
4 - Parâmetro nominal, obrigatório, com valor default (padrão).
5 - Parâmetro posicional e não obrigatório (args).
6 - Parâmetro nominal e não obrigatório (kwargs)"""

"""def converter_mes_para_extenso(data):
    mes = '''janeiro fereveiro março
    abril maio junho julho agosto
    setembro outubro novembro 
    dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1]
    return f'{d} de {mes_extenso} de {a}'


print(converter_mes_para_extenso('01/07/1988')) """


# DESAFIO
# funçao


def calcular_valor(valor, qnt, moeda='real', desconto=None, acrescimo=None):
    v_bruto = valor * qnt

    if desconto:
        v_bruto = v_bruto - (v_bruto * (desconto / 100))
    elif acrescimo:
        v_bruto = v_bruto + (v_bruto * (acrescimo / 100))

    if moeda == 'dolar':
        return 5.00 * v_bruto

    elif moeda == 'euro':
        return 5.70 * v_bruto
    elif moeda == 'real':
        return v_bruto
    else:
        print('Moeda não cadastrada')
        return 0


print(f"O valor final da conta é R$ {calcular_valor(valor=32, qnt=5, acrescimo=5)} reais")
