#Condições de pagamento
print('{:-^55}'.format(' \033[1;32mPAGAMENTO DE PRODUTO\033[m '))
print(' ')
valor = float(input('Digite o preço total dos produtos R$'))
print('''Selecione:
[ 1 ] à vista DINHEIRO/CHEQUE
[ 2 ] à vista no CARTÃO(débito) 
[ 3 ] em até 2X no CARTÃO 
[ 4 ] 3X ou mais no CARTÃO''')
opc = int(input('\033[4mForma de pagamento:\033[m '))
if opc == 1:
    desc = valor - (valor * 0.10)
    print('Valor total dos produtos: R${:.2f}'.format(valor))
    print('DESCONTO aplicado: 10%')
    print('\033[1;33mTOTAL:\033[m R${:.2f}'.format(desc))
elif opc == 2:
    desc = valor - (valor * 0.05)
    print('Valor total dos produtos: R${:.2f}'.format(valor))
    print('DESCONTO aplicado: 5%')
    print('\033[1;33mTOTAL:\033[m R${:.2f}'.format(desc))
elif opc == 3:
    vezes = int(input('Quantidade de parcelas(máximo 2x): '))
    print(' ')
    par = valor / vezes
    print('Valor total dos produtos: R${:.2f}'.format(valor))
    print('\033[1;37mPreço normal\033[m')
    print('\033[1;33mTOTAL em {}X:\033[m R${:.2f}'.format(vezes, valor))
    print('Valor da parcela: R${:.2f}'.format(par))
elif opc == 4:
    vezes = int(input('Quantidade de parcelas(3 até 10): '))
    print(' ')
    juros = valor + (valor * 0.2)
    par = juros / vezes
    print('Valor total dos produtos: R${:.2f}'.format(valor))
    print('JUROS aplicado: 20%')
    print('\033[1;33mTOTAL em {}X:\033[m R${:.2f}'.format(vezes,juros))
    print('Valor da parcela: R${:.2f}'.format(par))
else:
    print('\033[1;31mOpção inválida. Selecione novamente.\033[m')
