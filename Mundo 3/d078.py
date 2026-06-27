numeros=[]

for c in range(0,5):
    numeros.append(int(input(f'Digite o {c+1}° número: ')))

maior=max(numeros)
menor=min(numeros)

posiçaoM=[]
posiçaom=[]

for c, n in enumerate(numeros):
    if n==maior:
      posiçaoM.append(c)
    
    elif n==menor:
        posiçaom.append(c)
        
            
print(f'Você digitou os números: {numeros}\n')
print(f'O \033[31mMAIOR\033[m valor digitado foi o n° {maior} na(s) posição(ões): {posiçaoM}.')
print(f'O \033[34mMENOR\033[m valor digitado foi o n° {menor} na(s) posição(ões): {posiçaom}.')