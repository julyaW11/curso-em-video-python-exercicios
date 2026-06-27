num=list()
tabela=list()
i=0
j=0

for i in range(0,3):
    for j in range(0,3):
        num=input(f'Digite um número para a posição [{i+1},{j+1}]: ')
        
        tabela.append(num)
        

print('\n')

print('Tabela:')
print('-=-=-=--=--=--=-=-=-=-=-=--=-\n')
for i,c in enumerate(tabela):
    
    if i==0 or i==3 or i==6:
        print(f'| {c} |',end='')
    
    elif i==2 or i==5 or i==8: #esta linha pode sumir 
        print(f'| {c} |')
    
    else:
        print(f' {c} ',end='')
        
print('\n-=-=-=--=--=--=-=-=-=-=-=--=-\n')