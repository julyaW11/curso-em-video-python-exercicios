
print('Gerador de PA')
print('=*='*10)
primeirot=int(input('Diga o 1° termo da PA: '))
r=int(input('Diga a razão: '))

soma=primeirot
c=1
termoad=0
mais=10
while mais!=0:
    termoad=termoad+mais
    while c<=termoad:
        print('{}'.format(soma),end='')
        print('-'if c<termoad   else'',end=' ')
        soma+=r
        c+=1
    print('PAUSA')
    mais=int(input('Quantos termos mais você quer adcionar?'))    
print('\nFIM DO PROGRAMA')