
maior=0 
ho=0
muvin=0

while True:

    idade=int(input('Digite a idade da pessoa: '))
    sexo=str(input('Sexo [F/M]: ')).strip().upper()

    while sexo!='F' and sexo!='M':
        sexo=str(input('Sexo [F/M]: ')).strip().upper()

    if (idade>18):
        maior+=1

    if (sexo=='M'):    
        ho+=1

    if (sexo=='F') and (idade<20):
        muvin+=1

    con=str(input('Deseja continuar?[S/N]: ')).upper()

    while (con!='N') and (con!='S'):
        con=str(input('Deseja continuar?[S/N]: ')).upper()

    if (con=='N'):
        break


print(f'Tivemos {maior} pessoas maiores que 18 cadastradas')
print(f'{ho} homens cadastrados')
print(f'E {muvin} mulheres que possuem menos de 20 anos cadastradas')
        