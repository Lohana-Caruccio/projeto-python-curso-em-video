#Funções Moeda

def metade(num=0 or 0.0, f=False):
    res = num / 2
    return res if f is False else moeda(res) #Forma usada pela resolução do Gustavo Guanabara

def dobro(num=0 or 0.0, f=False):
    res = num * 2
    if f:
        v = moeda(res)
    else:
        v = res
    return v #Forma usada por mim para resolver

def aumentar(num=0 or 0.0, p=0, f = False):
    res = num + (num * (p / 100))
    if f:
        v = moeda(res)
    else:
        v = res
    return v

def diminuir(num=0 or 0.0, p=0, f = False):
    res = num - (num * (p /100))
    if f:
        v = moeda(res)
    else:
        v = res
    return v

def moeda(num=0 or 0.0, m = 'R$'):
    res = f'{m}{num:.2f}'.replace('.', ',') #Replace, troca todos os pontos por vírgulas
    return res

def resumo(num=0 or 0.0, a=10, d=5):
    print('-'*30)
    print('\033[36mRESUMO DO VALOR\033[m'.center(38)) #Colocou no centro
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(num)}') #\t para alinhar
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{a}% de aumento: \t{aumentar(num, a, True)}')
    print(f'{d}% de redução:  \t{diminuir(num, d, True)}')
    print('-'*30)