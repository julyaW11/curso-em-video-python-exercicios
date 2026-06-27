print('{:=^25}'.format('LOJAS JMTEC'))
produto=float(input('Preço da compra: R$ '))

print('FORMAS DE PAGAMENTO: ')
fpaga=int(input("""[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão

Qual a opção? """))

if fpaga==1:
    precf=produto - (produto*10)/100
    print('Com 10% de desconto', end=' ')

elif fpaga==2:
    precf=produto - (produto*5)/100
    print('Com 5% de de desconto', end=' ')

elif fpaga==3:
    precf=produto
    
elif fpaga==4:
    quantas=int(input('Em quantas parcelas: '))
    precf=produto + (produto*30)/100
    parcelas=precf/quantas
    print('Com 30% de JUROS e parcela mensal de {:.2f} '.format(parcelas), end=' ')
else :
    precf=0
    print('\033[31mOpção inválida de pagamento.Tente Novamente!\033[m')
print('a comprar custará R${:.2f}'.format(precf))