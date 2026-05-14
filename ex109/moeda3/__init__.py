#Funções Moeda2

def metade(num=0, f=False):
    res = num / 2
    return res if f is False else moeda(res) #Forma usada pela resolução do Gustavo Guanabara

def dobro(num=0, f=False):
    res = num * 2
    if f:
        v = moeda(res)
    else:
        v = res
    return v #Forma usada por mim para resolver

def aumentar(num=0, p=0, f = False):
    res = num + (num * (p / 100))
    if f:
        v = moeda(res)
    else:
        v = res
    return v

def diminuir(num=0, p=0, f = False):
    res = num - (num * (p /100))
    if f:
        v = moeda(res)
    else:
        v = res
    return v

def moeda(num=0 or 0.0, m = 'R$'):
    res = f'{m}{num:.2f}'.replace('.', ',') #Replace, troca todos os pontos por vírgulas
    return res
