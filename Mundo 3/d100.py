from random import randint

def sorteio():
    lista=[]
    lista=[randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100)]
    
    print(f'Os números sorteados foram: {lista}')
    return lista 

def somaPar(lista):
    
    soma=0
    
    for c in lista:
        if c%2==0:
            soma+=c
    
    print(f'A soma dos números PARES foi: {soma}')
    
    return 0

#Programa principal
somaPar(sorteio())
print()