print('GERADOR DE PA')
print(' ')
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0: #condição para finalizar o programa
    total += mais #começa com o mais para começar mostrando 10 termos e depois acumula a nova quantidade pedida
    while cont <= total:
        print('{}-> '.format(termo), end='')
        termo += r
        cont += 1
    print('-> PAUSA')
    mais = int(input('Quantos termos mais deseja mostrar? '))
print('\nProgressão finalizada com {} termos mostrados!'.format(total))


