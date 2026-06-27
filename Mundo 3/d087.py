num=list()
tabela=list()
slinha=list()
somapares=0
somatcoluna=0
i=0
j=0
c=0

for i in range(0,3):
    for j in range(0,3):
        num=int(input(f'Digite um número para a posição [{i+1},{j+1}]: '))
        
        tabela.append(num)
        

print('\n')

print('Tabela:')
print('-=-=-=--=--=--=-=-=-=-=-=--=-\n')
for i,c in enumerate(tabela):
    
    if i==0 or i==3 or i==6:
        print(f'| {c} |',end='')
    
    elif i==2 or i==5 or i==8:
        print(f'| {c} |')
    
    else:
        print(f' {c} ',end='')
        
print('\n-=-=-=--=--=--=-=-=-=-=-=--=-\n')

for c in tabela:
    if c%2==0:
        somapares=somapares+c
           

#Abaixo podemos fazer o seguinte---segunda linha---:
    #for i in range(0,3):
        #slinha += tabela[1][i]   
for i,c in enumerate(tabela):
    if i==2 or i==5 or i==8:
        somatcoluna=somatcoluna+c
    

#Abaixo podemos fazer o seguinte -----terceira coluna---:
    #for i in range(0,3):
        #slinha += tabela[i][2]
for i , c in enumerate(tabela):
    if i==3 or i==4 or i==5:
        slinha.append(c)
        
maior=max(slinha)


print(f'A soma de todos os números PARES DA TABELA são: {somapares}')
print(f'A soma de todos os números DA 3º COLUNA são: {somatcoluna}')
print(f'O MAIOR Nº DA SEGUNDA LINHA é o n°: {maior}\n')