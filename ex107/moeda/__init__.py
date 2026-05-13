#Funções Moeda

def metade(num):
    res = num / 2
    return res

def dobro(num):
    res = num * 2
    return res

def aumentar(num, p):
    res = num + (num * (p / 100))
    return res

def diminuir(num, p):
    res = num - (num * (p /100))
    return res
