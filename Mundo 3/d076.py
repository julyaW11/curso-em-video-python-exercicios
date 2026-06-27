produtos=('Mouse',50.00,'notebook',5500.00,'fone de ouvido',40.00,'caneta',2.50,
'corretivo',8.00,'caderno',12.30,'lápis',4.50,'grafite',12.00,'ticket',7.50,'borracha',5.60)
 7
 ´0
nomes=0

print('\n')
print('-=-'*18)
print(' '*16,end='')
print('LISTA DE PROUTOS')
print('-=-'*18)
print('\n')  or c in range(0,len(produtos)): 
    if c%2==0:
        print(produtos[c].capitalize(),end='')
        
        nomes=len(produtos[c])
        pontos=20-nomes
        print('.'*pontos,end='')

    elif c%2!=0:
        print(f'R$ {produtos[c]:2}')

print('\n')    



   

    
   