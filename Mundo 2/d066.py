
c=0
soma=0 

while True:
    n=int(input('Digite um número (999 para parar): '))

    if n==999:
        break
    else:
        c+=1
        soma+=n
            
print(f'Foram digitados {c} números, a soma entre eles resultou em {soma}' )