from datetime import date
ano=date.today().year

somai=0
somen=0
for c in range(0,7):
    nas=int(input('Diga o ano de nascimento da pessoa: '))
    idade=ano-nas

    if idade<18:
        somen=somen+1
    else:
        somai=somai+1

print('Há \033[31m{}\033[m pessoa(s) maiores de idade e \033[36m{}\033[m pessoa(s) de menor'.format(somai,somen))