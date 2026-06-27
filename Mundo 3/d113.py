def numeroInt(numI):
    
    while True:  
        try:
            numI = int(numI)
            return numI
        
        except ValueError:
                print('\033[31mVocê NÃO digitou um número inteiro.Tente novamente:\033[m' )     
                numI=input('Digite um número INTEIRO: ')   
                
            
                
                
def numeroFlt(numF):
    
    while True: 
        try:
            numF = float(numF)
            return numF

        except ValueError:
                print('\033[31mVocê NÃO digitou um número FLOAT.Tente novamente:\033[m' )     
                numF=input('Digite um número FLOAT: ')   
                
                
              
#Programa principal:        
numI = input('Digite um número: ') 
numI = numeroInt(numI)
print(f'Você digitou o número INTEIRO {numI}')
print(' ')
numF = input('Digite um número FLOAT: ')
numF = numeroFlt(numF)
print(f'Você digitou o número FLOAT {numF}')