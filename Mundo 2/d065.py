num = soma = c = media = menor = maior=0  
s=' '
while(s!='n'):
    num=int(input('Digite um número: '))
    c=c+1
    soma+=num
    
    if c==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num

        if num<menor:
            menor=num
    s=input('Deseja continuar digitando? [S/N] ').lower().strip()[0] #tô pegando a 1 letra 

media=soma/c  
print('Foram \033[36m{}\033[m números digitados e a soma entre eles resultou em \033[31m{}\033[m'.format(c,soma))
print('Maior n° foi o \033[35m{}\033[m e menor n° foi o \033[35m{}\033[m'.format(maior,menor))
print('\033[32mA média foi {}\033[m'.format(media))