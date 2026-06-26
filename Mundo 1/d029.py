velo=float(input('Diga a velocidade do carro: '))

if velo>80:
    print('Você ultrapassou a velocidade máxima pertimida de 80Km/h')
    multa=(velo-80)*7.00
    print('Você deverá pagar uma multa no valor de R${:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade permitida')

print('Tenha um bom dia!')
