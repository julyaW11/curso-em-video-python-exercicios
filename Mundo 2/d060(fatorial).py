num=int(input('Digite um número para saber seu Fatoiral: '))

c=num
mul=1
print('o FATORIAL de {} é: '.format(num))

print('{}!='.format(num),end=' ')
while c>0:
    print('{}'.format(c),end=' ')
    print('x' if c>1 else '=' ,end=' ')
    mul=c*mul
    c-=1
    
print('{}'.format(mul))