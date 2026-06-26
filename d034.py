sa=float(input('Digite seu salário:R$ '))

if sa<=1250 :
    aum=sa+(sa*15/100)
    print('Seu salario de {:.2f} com o aumento passará para {:.2f}'.format(sa,aum))
else :
    aum=sa+(sa*10/100)
    print('Seu de R${:.2f} com o aumento passará para R${:.2f}'.format(sa,aum))



