#Somatório de somente números ímpares e múltiplos de 3 no intervalo entre 1,500
soma = 0
cont = 0
for c in range(1,501,2):
        if c % 3 == 0:
            cont = cont + 1 # cont += 1
            soma = soma + c # soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))









