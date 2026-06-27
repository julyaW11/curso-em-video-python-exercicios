def dobro(n,mostra=False):

    double=n*2
    
    if mostra==False:
        return double
    else: 
        return f'R${double}'
    
#-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-    
def metade(n,mostra=False):
    divide=n//2
    
    if mostra==False:  
        return divide
    else:
         return f'R${divide}'
     
#-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def aumenta(n,mostra=False):
       
    dezpcento=(n*10)/100
    total=n+dezpcento
    
    if mostra==False:
        return total
    
    else:
        return f'R${total}'

#-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def diminui(n,mostra=False):
    trezepcento=(n*13)/100
    total=n-trezepcento
    
    if mostra==False:
        return total
    
    else:
        return f'R${total}'
    
#-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def monetario(n):
    return f'R${n}'