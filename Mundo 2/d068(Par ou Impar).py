from random import randint 

jogador=0
vi=0

while True:
    comp=randint(0,10)
    jogador=int(input('Digite um número: '))
    pi=str(input('Você quer Par ou Impar? [I/P]: ')).strip().upper()

    while pi!='P' and pi!='I':
         pi=str(input('Você quer Par ou Impar? [I/P]: ')).strip().upper()

    soma=jogador+comp 

    print(f'Você jogou \033[33m{jogador}\033[m e o Computador escolheu \033[33m{comp}\033[m.',end='')

    if soma%2==0:
        print(' O resultado deu \033[36mPAR\033[m')
        
        if pi=='P':
            print('\033[33mVocê venceu!!Vamos para próxima rodada!\033[m')
            vi+=1
        else: 
            break 
        
    elif soma%2!=0:

        print('O resultado deu \033[36mIMPAR\033[m')

        if pi=='I':
            print('\033[33mVocê venceu!!Vamos para próxima rodada!\033[m')
            vi+=1
        else: 
            break 

print(f'\033[31mGAME OVER\033[m.Você venceu {vi} veze(s)')
