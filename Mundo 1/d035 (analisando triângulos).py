reta1=int(input('Diga o comprimento da primeira reta: '))
reta2=int(input('Diga o comprimneto da segunda reta: '))
reta3=int(input('Diga o comprimento da terceira reta: '))

umdo=reta1+reta2
umtr=reta1+reta3
dotr=reta2+reta3

if umdo>reta3 and umtr>reta2 and dotr>reta1:
    print('As retas formam um triangulo')
else: 
    print('As retas NÃO formam um triângulo')

