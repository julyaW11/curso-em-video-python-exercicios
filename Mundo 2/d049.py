num=int(input('Digite um número: '))

print('\033[31mA TABUADA DO {} É: \033[m'.format(num))
for c in range(1,11):
    print('\033[36m{} X {} = {}\033[m'.format(num,c,c*num))
