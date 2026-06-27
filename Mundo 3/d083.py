
expressao= str(input('Digite uma expressao matematica: '))
pilha=[]
tam=len(expressao)

for c in expressao:
    if c=='(' :
        pilha.append('(')
        
    elif  c==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            
        
    
    
if len(pilha)==0:
    print('Sua expressão está CORRETA!')
    
else:
    print('Sua expressão está INCORRETA!')
        
        