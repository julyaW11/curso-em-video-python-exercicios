from random import randint , choice
from time import sleep 

print('\033[36;47mOi eu sou seu computador, vamos brincar?\033[m')
print('Eu pensei num número entre 0 e 10. Você consegue adivinhar?')
comp=randint(0,10)

jog=int(input('Diga o número que você pensou: '))
print('Analisando.....')
sleep(2)


if jog==comp:
  print('\033[36mPARABÈNS, você acertou o número!Bela jogada!\033[m')


else: 
  ('O computador ganhou!O número escolhido foi: {}.\033[31mTente novamente!\033[m'.format(comp))