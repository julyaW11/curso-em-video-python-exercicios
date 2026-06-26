print('Um determinado produto, se comprado à vista, o comprador tem direito à 10% de desconto.',end='')
print('Se comprado parcelado o preço aumenta em 8%.')
preco=float(input('Digite o preço do produto:R$'))
avista=preco-(preco*10/100)
parce=preco+(preco*8/100)

print('À vista o produto custa R${:.2f} e parcelado custa R${:.2f}'.format(avista,parce))
