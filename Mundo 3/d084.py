lista=list()
cadastro=[]
maxi=mini=0
maior=list()
menor=list()

while True:
    
    lista.append(str(input("Digite seu nome: ")))
    lista.append(int(input("Digite seu peso: ")))
    
    
    if len(cadastro)==0:
        mini=lista[1]
        maxi=lista[1]

    else:
        if lista[1]>maxi:
            maxi=lista[1]
           
            
        elif lista[1]<mini:
            mini=lista[1]
            

    cadastro.append(lista[:])
    lista.clear()
    s=str(input('Deseja continuar?[S/N]: '))
    
    if s in 'Nn':
        break 

print(f'Ao todo você cadastrou {len(cadastro)} pessoas')

for c in cadastro:
    if c[1]==maxi:
        maior.append(c[0])
    
    elif c[1]==mini:
        menor.append(c[0])
        
print(f'A(s) pessoa(s) mais LEVES foi/foram {menor}')
print(f'A(s) pessoa(s) mais PESADOS foi/foram {maior}')            