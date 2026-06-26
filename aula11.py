from time import sleep

print('VAMOS BRINCAR COM AS CORES DO TERMINALLLLL\n')

print(' E PARA BRINCAR, VAMOS USAR A FRASE OLÁ,MUNDO \n\n')


print('\033[30;46m Olá, mundo!')

#print('NO EXEMPLO DE CIMA VIMOS QUE O FUNDO COLORE ALÉM DA FRASE, CASO NÃO ACHE ESTETICAMENTE BONITO, TAMBEM PODEMIS FAZER:')
print('\033[4;30;45m Olá, Mundo!\033[m')
print('\033[30;41m Olá, Mundo!\033[m')
print('\033[4;35;47m Olá Mundo\033[m')

print('\033[34m-=-\033[m'*20)


print('AGORA VAMOS APRENDER COMO USAR CORES EM VARÁVEIS/PONTOS ESPECÍFICOS DA FRASE\n')
sleep(6)

#Primeiro Jeito
a=3
b=5
print('Os números \033[34m{}\033[m e \033[32m{}\033[m são números \033[33mIMPARES\033[m'.format(a,b))

#O formato acima pode gerar confusão e não ser prático em códigos longos, então temos mais duas opções

#Segundo jeito:

nome='Júlia'
print('Olá {}{}{}, você tem um belo nome!\n\n'.format('\033[36m',nome,'\033[m'))

#Terceiro Jeito: este jeito aki vamos trabalhar mais pra frente. AQUI USAREMOS OS CHAMADOS DICIONÁRIOS

cores={'limpa':'\033[m' , 'magema':'\033[35m', 'pretoebranco':'\033[7;47m' , 'vermelho':'\033[31m'}
nome1='Júlia'
nome2='Peu'
nome3='sex on the beach'

print('Olá {}{}{}, Muito Prazer em te conhecer'.format(cores['magema'],nome1,cores['limpa']),end=' ')
print('eu soube que você tem com cachorrinho muito fofo chamada {}{}{}\n'.format(cores['pretoebranco'],nome2,cores['limpa']))
print('Eu sei qual sua bebida preferida.....ummmm deixe-me lembrar')
sleep(3)
print('Lembrei! Sua bebida favorita é  o drink {}{}{}\n'.format(cores['vermelho'],nome3,cores['limpa']))

print('Foi ótimo conversar com você, até mais ;)')