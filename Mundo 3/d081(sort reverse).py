nu = []
sn='s'
c=0
posiçao = 0 


while sn in 'Ss':
    n=int(input('Digite um número: '))
    c+=1
    nu.append(n)      
    sn=str(input('Deseja continuar?[S/N] ')).lower()
    
nu.sort(reverse=True)
    

print(f'Você digitou a seguinte lista:{nu}')
print(f'Você digitou {c} número(s).')

if 5 in nu: 
    print(f'O número \033[32m5\033[m apareceu  na(s) posição(ões) {find(nu,5)}.')

else:
    print(f'O numero \033[32m5\033[m NÃO aparece na lista.')