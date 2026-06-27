cadastro=[]
peso=list()
nome=list()

while True:
    nome.append(str(input("Digite seu nome: ")))
    peso.append(int(input("Digite seu peso: ")))
    cadastro.append(nome[:]) # tinha que criar uma copiaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa
    cadastro.append(peso)
    
            
    sn=str(input("Deseja continuar?[S/N] "))
    
    if sn in 'Nn':
        break
    
  
quantidade=len(peso)
print(f'O número de pessoas cadastrada foi: {quantidade}')

maispesado=list()
maisleve=list()

media=sum(peso)/ quantidade

for i, c in enumerate(peso):
    if c > media:
        maispesado.append(nome[i])
    
    elif c < media:
        maisleve.append(nome[i])
    

print(f'A(s) pessoa(s) mais de MENOR PESO é/são:{maisleve}')
print(f'A(s) pessoa(s) mais MAIOR PESO é/são:{maispesado}')
        
        
        
         
                
#print(f'A(s) pessoa(s) mais PESADAS foi(foram): {maispesadas}')
#print(f'A(s) pessoa(s) mais LEVES foi(foram): {maisleves}')

