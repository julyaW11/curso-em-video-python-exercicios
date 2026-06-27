num=0
soma=0
c=0

while(num!=999):
    num=int(input('Digite um número [999 para parar]: '))
    c=c+1
    soma+=num

somaf=soma-999
print('Foram digitados {} números'.format(c))
print('A soma desses números é {}'.format(somaf))

