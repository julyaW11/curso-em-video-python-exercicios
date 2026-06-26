n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
m=(n1+n2)/2

print('Sua média foi {:.2f}'.format(m))

if m>=7:
    print('Você está passado nesta matéria')
else:
    print('Você está reprovado, final sera dia 02/11')

#Usando CONDIÇÃO SIMPLIFICADA:

print('Precisa de pouco para passar de ano'if m>=6 else'Precisa de muitos pontos para passar de ano')
