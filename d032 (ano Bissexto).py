from datetime import date
ano=int(input('Qual ano Você quer analisar?\nCaso queira sbaer se o ano atual é Bissexto, digite 0: '))


if ano==0:
    ano=date.today().year

#Um ano BISSEXTO é divisível por 4 EXCETO os números mútiplos de 100 que NÃO SÃO multiplos de 400
# OU SEJA, anos bissextos são números DIVISÍVEIS POR 4 E POR 400 E NÃO DIVISÍVEIS POR 100 
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('{} é um ano bissexto'.format(ano))
else :
    print('{} NÃO é um ano bissexto'.format(ano))
