#Calculando a média do aluno
print('\033[4;35mCALCULANDO A MÉDIA\033[m')
print(' ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Você foi APROVADO! Sua média foi {:.1f}'.format(media))
elif media < 5:
    print('Você foi REPROVADO! Sua média foi de {:.1f} e o mínimo era {}'.format(media,7.0))
else:
    print('Você pegou RECUPERAÇÃO! Sua média foi {:.1f} e o mínimo era {}'.format(media,7.0))