preço = float(input('Digite o preço do produto: R$'))
des = (preço * 5/100)
novovalor = preço - des
print('O valor desse produto, que era R${:.2f}, com desconto de 5% na promoção,\nficará R${:.2f}!'.format(preço,novovalor))