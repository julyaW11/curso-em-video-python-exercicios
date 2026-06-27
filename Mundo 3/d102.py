#Função
def fatorial(num=1,mostra=False):
    """FATORIAL:
    ->Esta função calcula o fatorial de qualquer número
    ->Tem como opcional o parâmetro "mostra" que mostra a multiplicação e não apenas o resultado.
    """
    soma=1
    for c in range(num,0,-1):
        soma=soma*c
        
        if mostra==True : #if mostra:
            print(f'{c}', end='')  
            
            
            if c>1:
                print(' X ',end='')
            
            else:
                print(' = ', end='')
                
    
    print(soma)
    
        
#Programa principal
print(fatorial(5,mostra=True))
print(fatorial(9))
help(fatorial)