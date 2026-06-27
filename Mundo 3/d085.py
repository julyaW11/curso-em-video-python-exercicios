num=list()
pares=list()
impares=list()
c=0


for c in range(0,7):
    num.append(int(input(f'Digite um número para {c+1}º posição: ')))
        

for c in num:  
    if c%2==0:
        pares.append(c)
        
    else:
        impares.append(c)
   
pares.sort()
impares.sort()        
        
print('\nPARES: ')

print(pares)
print('-=-=-=--=--=--=-=-')

print('\nIMPARES: ')

print(impares)
print('-=-=-=--=--=--=-=-\n')