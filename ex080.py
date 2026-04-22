#Lista ordenada sem repetições
lista = list()
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]: #Aqui ele confere se c == 0, coloca o valor na última posição,
        lista.append(valor) # mas se o valor for maior do que o que já estiver na última posição,
        print('Adicionado ao final da lista...') #o novo número será colocado. Se não for nenhum desses dois casos...
    else:
        pos = 0
        while pos < len(lista): #varre desde a primeira pos até a última se necessário
            if valor <= lista[pos]: #se o valor for menor que o valor já colocado na posição [0], isso é igual lista[0]
                lista.insert(pos, valor) #ele vai inserir o novo valor na posição
                print(f'Adicionado na posição {pos} da lista...')
                break #o break acontece se tiver sido encontrado a posição do número, se não, ele vai consultar a próxima posição
            pos += 1 #se necessário ele vai começar o loop novamente, mas consultando a pos [1], se não a 2, 3...
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')