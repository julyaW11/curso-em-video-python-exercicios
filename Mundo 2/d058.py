from random import randint 
from time import sleep 


print("""\033[47;31mOla eu sou seu computador. Vamos jogar?
Eu pensei num número entre 0 e 10 
Você consegue advinhar qual é? ;D\033[m

""")
comp=randint(1,10)
c=0
acertou=False #por letra MAIÚSCULA

while not acertou: 
    c+=1
    usu=int(input('Digite um número: '))

    if usu<comp:
        print('Chute um pouco mais alto...\033[31mTente Novamente\033[m')

    elif usu>comp:
         print('Chute um pouco mais baixo...\033[31mTente Novamente\033[m')

    if usu==comp:
        acertou=True
        print('\033[36mPARABÊNS!Você acertou\033[m')
print('Foram necessárias {} tentativas'.format(c))