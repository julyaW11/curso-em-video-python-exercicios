from time import sleep
num=int(input('Digite um número: '))
qdi=0
sleep(1)

print('Avaliando os números: ')
print('-=-'*20)

for c in range(1,num+1):
    if num%c==0:
        print('\033[31m ', end= ' ') #podemos por cores no terminal deste jeito
        qdi+=1
    else:
        print('\033[34m ',end= ' ') 
    print('{}'.format(c),end=' ')

if qdi==2:
    print('\n\033[mSendo divisível {} veze(s), o número {} É PRIMO'.format(qdi,num)) 
    #colocando o \n e o \033[m ANULAMOS o comando de cores e aproximação das frases do print acima

else:
    print('\n\033[mSendo divisível {} veze(s), o número {} NÃO É PRIMO'.format(qdi,num))