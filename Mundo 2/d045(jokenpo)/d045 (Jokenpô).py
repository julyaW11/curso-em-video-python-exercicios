from random import choice
from time import sleep

print('OLÁ eu sou seu Computador! Vamos brincar de \033[37;45mPEDRA,PAPEL ou TESOURA?\033[m')
#print()
lista=['pedra','papel','tesoura']
comp=choice(lista)
cont = 'S'

while cont!='N': 
    usu=str(input('Diga qual você escolheu ;D :')).lower()

    sleep(2)
    print('Bora lá?')
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(2)

    if usu==comp:
        print('\033[32;47mEita, tivemos um empate.\033[m')
        print('O computador também escolheu {}'.format(comp))

    elif usu=='pedra' and comp=='tesoura' or usu=='papel' and comp=='pedra' or usu=='tesoura' and comp=='papel':
        print('\033[36mPARABÉNS\033[m, você ganhou.O computador escolheu \033[33m{}\033[m'.format(comp))
        print('\033[7mBoa jogada!\033[m')

    else:
        print('\033[47;31mO computador ganhou!\033[m')
        print('\033[31;47mO computador escolheu {}\033[m'.format(comp))
        print('\033[47;36mTente outra vez!\033[m')

    cont = str(input('Quer jogar novamente? [S/N]')).strip().upper()