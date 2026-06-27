soma=0
cont=0
for c in range(0,6): 
    num=int(input('Digite um número: '))
    if num%2==0:
        cont+=1
        soma+=num
print('Você digitou {} n° PARES e a soma foi: {}'.format(cont,soma))