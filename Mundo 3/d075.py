

tupinteira=(int(input('Digite o 1° valor: ')),int(input('Digite o 2° valor: ')),int(input('Digite o 3° valor: ')),int(input('Digite o 4° valor: ')))

 
c9=tupinteira.count(9)
if c9==0: 
    print(f'\nO N° 9 aparece NÃO foi digitado')

else: 
    print(f'\nO N° 9 aparece {c9} vez(es)')



p=0
for c1 in range(0,len(tupinteira)): 
    if tupinteira[c1]%2==0:
        p+=1

if p==0:
    print('NÃO foram digitados números PARES') 

else: 
    print('O(s) número(s) PAR(ES) é(são): ',end='')

for c in range (0,len(tupinteira)): 
    if tupinteira[c]%2==0: 
        print(tupinteira[c],end=' ')

        

if 3 in tupinteira: 
    print(f'\nO n° 3 aparece primeiro na {tupinteira.index(3)+1}° posição.')
else: 
    print('\nO n° 3 NÃo foi digitado.') 