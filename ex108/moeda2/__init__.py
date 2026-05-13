#Funções

def metade(num=0):
    res = num / 2
    return res

def dobro(num=0):
    res = num * 2
    return res

def aumentar(num=0, p=0):
    res = num + (num * (p / 100))
    return res

def diminuir(num=0, p=0):
    res = num - (num * (p /100))
    return res

def moeda(num=0, m = 'R$'):
    res = f'{m}{num:.2f}'.replace('.', ',') #Replace, troca todos os pontos por vírgulas
    return res
