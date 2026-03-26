frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição {}'.format(frase.find('A')))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')-frase.count(' ')))