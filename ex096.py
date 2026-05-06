#Função que calcula área
print(f'{"CONTROLE DE TERRENOS":^35}')
print('-'*35)
def area(l, c):
    ar = l * c
    print(f'\nA área de um terreno {l:.1f} x {c:.1f} é de {ar}m²!')

#Programa principal
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura,comprimento)
