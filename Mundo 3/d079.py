nu=[]
nu.append(int(input('Digite um número: ')))
print('Número adicionado com sucesso. ')
r='S'

while (r in'Ss'):
        
    r=input('Deseja continuar?[S/N]: ')
    if r in 'Nn':
        break 
    
 
    t=int(input('Digite um número: '))
      
    if t in nu: 
        print('Este número já foi digitado. Não irei adicionar.')
        
    else: 
        print('Número adicionado com sucesso. ')
        nu.append(t)
        
    

nu.sort()
print(f'Você digitou os número(s) {nu}') 