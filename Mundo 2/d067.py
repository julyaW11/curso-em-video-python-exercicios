n=0 
c=0
print('\033[36mCALCULANDO TABUADA\033[m')
print('-=-'*10)
while n>=0:
    n=(int(input('Digite um número: ')))

    if n<0:
        break

    else:

        for c in range(1,11): 
            print(f'{n} X {c} = {n*c}')
    
    