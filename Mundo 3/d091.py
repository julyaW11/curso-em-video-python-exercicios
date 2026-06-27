from random import randint
from time import sleep

jogadores=dict()

jogadores={'jogador_1':randint(0,10),'jogador_2':randint(0,10),'jogador_3':randint(0,10),'jogador_4':randint(0,10)
           ,'jogador_5':randint(0,10),'jogador_6':randint(0,10) }

for k , v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
    
ordem=sorted(jogadores.items(),key=lambda x: x[1],reverse=True)

print('-=-'*10)


c=1
for k , v in ordem:
    print(f'O {c}° lugar: {k} com {v}')
    c+=1
    sleep(1)

print('\n')