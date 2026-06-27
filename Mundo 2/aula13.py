from time import sleep
i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))

for c in range(i,f+1,p):
    print(c)
print('Fim')
sleep(2)

s=0
for c in range(0,4): #contando 0, 1 , 2 e 3 dá 4 repetições.
    n=int(input('Digite um número: '))
    s+=n # isto equivale á s=s+n
print('O somatório dos números é {}\n\n'.format(s))

#indo de trás pra frente temos:

sleep(2)

for c in range(6,0,-1): # este menos -1 é a iterlação, ao seja a forma como o programa deve andar. 
    print(c)
print('Fim')