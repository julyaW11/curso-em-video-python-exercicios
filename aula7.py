print('VAMOS BRINCAR UM POUCO COM O FORMAT\n')

nome=input('Qual se nome?')
print('Prazer em te conhecer {}!\n'.format(nome))

print('aki vamos fazer o nome aparecer apos 20 espaços')
nome1=input('Qual seu segundo nome?')
print('É um belo nome {:20}!!!\n'.format(nome1))

print('com isso nos podemos usar alinhamento')
print(' agora vamos alinhar Á DIREITA em 20 espaços')
nome2=input('Também quero saber seu sobrenome:')
print('ummm tereçante o sobrenome {:>20}!\n'.format(nome2))

print('alinhando Á ESQUERDA em 20 espaços')
nome3=input('Soube que você tem um cachorrinho,qual o nome dele?')
print('Owwwwwww que fofinho o nome {:<20}!\n'.format(nome3))

print(' agora vamos centralizar')
nome4=input('Seu cachorro tem sobrenome?')
print('Olá Pepeto {:^20}!\n'.format(nome4))

print('agora vamos centralizar printando os = ')
nome5=input('Diga um nome que você acha bonito:')
print( '{:=^20}\n'.format(nome5))

print('É necessario colocar os :,caso isto não seja feito teremos a situação abaixo que irá resultar em error')
nome12=input('Diga seu nome:')
print('Olá {20}'.format(nome12))
