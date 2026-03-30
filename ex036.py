# Empréstico bancário para casa
print('-'*26)
print('\033[4;33mANALISANDO SEU EMPRÉSTIMO\033[m')
print('-'*26)
valor = float(input('Digite o valor da casa que você deseja fazer o empréstimo R$ '))
salario = float(input('Digite o valor do seu  salário atual R$ '))
anos = int(input('Em quantos anos deseja pagar: '))
prestacao = valor / (anos * 12)
if prestacao > salario * 30 / 100:
    print('\033[1;31mEmpréstimo negado\033[m, a parcela passará de 30% do seu salário!')
else:
    print('\033[1;36mEmpréstimo aprovado!\033[m\nO valor da parcela ficará R${:.2f} por mês pelos próximos {} anos!'.format(prestacao,anos))