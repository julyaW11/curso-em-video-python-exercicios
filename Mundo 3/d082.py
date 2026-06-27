
lista = []
par = []
impar = []
continua='Ss'

while continua in 'Ss': 
    n = input(int('Digite um número: '))
    lista.append(n)
    
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    
    continua=input('Deseja continuar? [S/N]')

print(f'Você digitou a seguinte lista: \033[31m{lista}\033m')
print(f'Os números PARES digitados foram: \033[35m{par}\033[m')
print(f'Os números ÍMPARES digitados foram: \033[35m{impar}\033[m')