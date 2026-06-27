from time import sleep

def maior(*numeros):
    
    
    if not numeros: #"Se a tupla estiver vazia"
        print(f'Os números informados foram: ')
        sleep(1)
        print(f'O -maior- valor informado foi 0.')
    
    else:     
        print(f'Os números passados foram: ')
        sleep(1)
        
        for c in numeros:
            print(c,end=' ') 

        quantidade=len(numeros) 
        maior=max(numeros) 
        
        print(f', foram informados {quantidade} valores ao todo.')
        sleep(1)
        print(f'O -maior- valor informado foi {maior}.')
        sleep(1)
        print('-=-'*20)
        
        
            

        
#Programa Principal        
maior(1,2,3,4,5)
maior(200,0,3)
maior(3,6,5,8,0)
maior(1,2,3)
maior(0)
maior()