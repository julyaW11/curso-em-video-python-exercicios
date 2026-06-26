from random import randint
from time import sleep
print('Ola, eu sou seu computador')
print('Eu pensei em um número entre 0 e 5')
print('Você consege dizer qual é este número?')
m=randint(0,5)
nusu=int(input('Diga qual número você acha que eu pensei ;D: '))

print('ANALISANDO....')
sleep(2)
if m==nusu:
    print('PARABÉNS, VOCÊ ACERTOU!')
    print('O número escolhido foi {}'.format(nusu))
else:
    print('O computador venceu')
    print('O número escolhido foi {}'.format(m))