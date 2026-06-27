from time import sleep
nu=[] 

for c in range(0,5):
    n = int(input(f'Digite o {c+1}° numero: '))
    
    if c==0 or n> nu[-1]: #lembrando que -1 se refere ao ULTIMO elemento. 
        nu.append(n)
        
    else:
        posiçao=0 
        while posiçao <= len(nu):
            if n<= nu[posiçao]:
                nu.insert( posiçao, n)
                break
            posiçao+=1
                
print('\033[31mCarregando....\033[m')   
sleep(2)
print(f'Você digitou a lista: {nu}')   