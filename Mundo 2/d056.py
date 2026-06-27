mvelho=0
nomemv=''
m20=0
somaid=0

for c in range(1,5):
    print('-=-=-{}° PESSOA-=-=-'.format(c))
    nome=str(input('Digite o nome: '))
    sexo=str(input('Digite H para homem e M se for mulher: ')).lower().strip() #CIMA
    idade=int(input('Diga a idade: '))

    somaid+=idade
    media=somaid/4

    if c==1 and sexo=='h': #podemos colocar IF C==1 AND SEXO **IN** 'Hm' (com isso não precisamos por LOWER ali em cima)
        mvelho=idade       #MANTEMOS O STRIP
        nomemv=nome            

    if sexo=='h' and idade>mvelho:
        mvelho=idade
        nomemv=nome

    if sexo=='m' and idade<20: #podemos colocar IF C==1 AND SEXO **IN** 'Mm' (com isso não precisamos por LOWER ali em cima)
        m20=m20+1              #MANTEMOS O STRIP

print('A média de idade é de {:.1f} anos'.format(media))   
print('O homem mais velho é {} com {} anos'.format(nomemv.upper(),mvelho))
print('{} mulhere(s) têm menos de 20 anos'.format(m20))