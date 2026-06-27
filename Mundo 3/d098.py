from time import sleep

def contador(inicio,fim,pulo):
    print()
    
    print(f'Contagem de {inicio} até {fim} pulando de {pulo} em {pulo}: ')
    
    if pulo==0:
        print(f'{inicio} , {fim} em {pulo}')
        print(f'{inicio} {fim} FIM!')
    
    
    elif pulo>0 and inicio<fim: 
        for c in range(inicio,fim+1,pulo):
            print(f'{c}',end=' ')
    
        print('FIM!') 
        
    
    elif pulo<0: 
        for c in range(inicio,fim-1,pulo):
            print(f'{c}',end=' ')
    
        print('FIM!')
         
    
    elif inicio>fim:
        for c in range(inicio,fim-1,-pulo):
            print(f'{c}',end=' ')
    
        print('FIM!')
        print('-=-'*15)
    
    
      

contador(1,10,1)
print()
contador(10,0,2)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-
sleep(1)
print()
begin=int(input('Digite o n° inicial que você deseja inserir: '))
endd=int(input('Digite o n° final que você deseja inserir: '))
jumpp=int(input('Digite de quanto em quanto o contador deve mostrar: '))

contador(begin,endd,jumpp)
