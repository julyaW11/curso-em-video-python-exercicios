
def numero(numb):
    
    if numb.isalpha() or numb.strip()=='':
        while numb.isalpha() or numb.strip()=='':
            numb=str(input('\033[31mERRO! Digite um número inteiro:\033[m '))
            
            if numb.isdigit():
                return numb
    
    else:
        return numb
    
#Programa principal:        
num = numero(input('Digite um número: '))   
print(f'O número que você acabou de digitar foi {num}')

#Funçao
# def numero(numb):
    
#     if numb.isalpha():
#         while numb.isalpha():
#             numb=str(input('\033[31mERRO! Digite um número inteiro:\033[m '))
            
#             if numb.isdigit():
#                 print(f'O número que você acabou de digitar foi o número {numb}')
#                 break
                
        
    
#     else:
#         print(f'O número que você acabou de digitar foi o número {numb}')
        
#     return None


# num=input('Digite um número: ')
# numero(num)
      