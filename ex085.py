#Listas com pares e ímpares
total = [[], []]
valor = 0
for c in range(1,8):
   valor = int(input(f'Digite o {c}º valor: '))
   if valor % 2 == 0:
       total[0].append(valor)
   else:
       total[1].append(valor)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(total[0])}')
print(f'Os valores ímpares digitados foram: {sorted(total[1])}')
