#Exercitando módulos em Python com formatação chamando função moeda dentro das outras funções

import moeda3

p = float(input("Digite o preço do produto: R$"))
print(f'A metade de {moeda3.moeda(p)} é {moeda3.metade(p, True)}.')
print(f'O dobro de {moeda3.moeda(p)} é {moeda3.dobro(p, True)}.')
print(f'Aumentando 10%, temos {moeda3.aumentar(p, 10, True)}.')
print(f'Reduzindo 13%, temos {moeda3.diminuir(p, 13, True)}.')

