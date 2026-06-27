from random import randint
from time import sleep

sorteiototal=list()
sorteio=list()
jogos=0


jogos=int(input('Quantos jogos você deseja jogar?: '))
print('')
print('=-=-=-=-SORTEANDO-JOGOS-=-=-=-=')
for c in range(0,jogos):
    sorteio=(randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60))
    sorteiototal.append(sorteio)
    
 
for i,c in enumerate(sorteiototal):
    print(f'{i+1}° Jogo: {c}')
    sleep(1)

print('-=-=-=--=-=Boa Sorte=-=-=-=-=-')
print('\n')