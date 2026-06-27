n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))

maior=n1
if n1>n2:
    print('\033[36m{}\033[m é o maior número'.format(maior))
elif n2>n1:
    maior=n2
    print('\033[36m{}\033[m é o maior número'.format(maior))
else :
    print('\033[31mOs dois números são iguais!\033[m')