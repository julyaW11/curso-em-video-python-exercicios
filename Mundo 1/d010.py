reais=float(input('Quantos reais você tem na carteira? R$'))
dolar=reais/5.85 #neste dia tava 5.40
euro=reais/5.56
pesosa=reais/0.071
pesosc=reais/0.0064
print('Com esta quantia:\n', end=' ')
print('Você pode comprar {:.2f} dolares'.format(dolar))
print('Você pode comprar {:.2f} euros'.format(euro))
print('Você pode comprar {:.2f} pesos argentinos'.format(pesosa))
print('Você pode comprar {:.2f} pesos chilenos'.format(pesosc))


