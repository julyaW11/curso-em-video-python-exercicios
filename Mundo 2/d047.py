from time import sleep
print('\033[31mOs números pares entre 1 e 50 são: \033[m')

for c in range(1,51): 
    if c%2==0:
        print(c,end=' ')
print('\033[33mACABOU!\033[m')

sleep(3)
print('\033[47;31mTAMBÉM PODEMOS FAZER: \033[m')

for c in range(2,51,2):
    print(c,end=' ')
print('ACABOU 2.O!')

#JÁ SABENDO que o programa pula de dois em dois por conta dos números serem pares
# fazendo assim reduzimos pela metade o tempo que o processador para executar este programa