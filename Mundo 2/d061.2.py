print('Gerador de PA')
print('=*='*10)
primeirot=int(input('Diga o 1° termo da PA: '))
r=int(input('Diga a razão: '))

soma=primeirot
c=1
while c<=10:
    print('{}'.format(soma),end='')
    print('-'if c<10   else'',end='')
    soma+=r
    c+=1
print('\nFIM DO PROGRAMA')