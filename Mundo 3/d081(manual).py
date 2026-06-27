nu = []
sn='s'
c=0
posiçao = 0 


while sn in 'Ss':
    n=int(input('Digite um número: '))
    
    

    if c==0 or n<nu[-1]:
        nu.append(n)
         
        
    else:
        posiçao=0
        while posiçao <= len(nu):
            if n >= nu[posiçao]:
                nu.insert(posiçao,n)
                break
            posiçao+=1
    
    c+=1 
             
        
    sn=str(input('Deseja continuar?[S/N] ')).lower()
    

    

print(f'Você digitou a seguinte lista:{nu}')
print(f'Você digitou {c} número(s).')

if 5 in nu: 
    print(f'O número \033[32m5\033[m apareceu  na(s) posição(ões) {find(nu,5)}.')

else:
    print('O numero \033[32m5\033[m NÃO aparece na lista.')

         
