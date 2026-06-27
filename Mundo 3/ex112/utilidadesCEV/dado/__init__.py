def confere(p):
    
    if p is str:
        while True:
            print(f'\033[31;mERRO!: "{p} é um preço inválido.\033[m"')
            p=input('Digite o preço: R$ ')
            
            if p.isnumeric():
                return p
                 
    
    else: 
        return p      

