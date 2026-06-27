num=int(input('Digite um número: '))

print('A sequência de Fibonnaci do número {} é: '.format(num))

if num==1:
    print('0-1-1')

elif num==2:
    print('0-1-1-2')
    
else:
  
  
  print('0-1',end='-')

  soma=0
  soma1=0
  detras=1
  while detras<num:
    soma=detras+soma1
    detras=soma-soma1
    soma1=soma
    if detras<num:
        print('{}'.format(soma),end='-')   
        soma=0  
        
        
    else:
      print('{}'.format(num))
      