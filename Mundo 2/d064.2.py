num=int(input('Digite um número [999 para parar]: '))
soma=0
c=0
while(num!=999):
    c=c+1
    soma+=num
    num=int(input('Digite um número [999 para parar]: '))

print('Foram digitados {} números'.format(c))
print('A soma desses números é {}'.format(soma))

