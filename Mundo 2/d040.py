nota1=float(input('Digite aqui sua 1° nota: '))
nota2=float(input('Digite aqui sua 2° nota: '))

media=(nota1+nota2)/2

print('Com média {:.2f}'.format(media))

if media<5.0:
    print('Você está \033[31mReprovado\033[m')
elif media>=5.0 and media<=6.9:
    print('Você está em \033[33mRecuperação\033[m,estude para a final.')
else :
    print('\033[36mParabéns, você está aprovado!\033[m')

