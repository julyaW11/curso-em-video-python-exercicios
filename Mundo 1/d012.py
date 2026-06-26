preco=float(input('Dê o preço do produto: R$'))
novo=preco-(preco*5/100)
print('Com 5% de desconto, o produto  passa a valer R${:.2f}'.format(novo))
