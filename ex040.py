#Calculando a média do aluno
print('\033[4;35mCALCULANDO A MÉDIA\033[m')
print(' ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Aprovado! Sua média foi {:.1f}'.format(media))
elif media < 5:
    print('Reprovado! Sua média foi de {:.1f} e o mínimo era {}'.format(media,7.0))
else:
    print('Recuperação! Sua média foi {:.1f} e o mínimo era {}'.format(media,7.0))