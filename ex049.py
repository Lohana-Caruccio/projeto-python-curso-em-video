#Tabuada de um número
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {:2}'.format(n,c,c* n))

