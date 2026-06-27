reta1=int(input('Digite o comprimeneto da 1° reta: '))
reta2=int(input('Digite o comprimeto da 2° reta: '))
reta3=int(input('Digite o comprimento da 3° reta: '))

umdo=reta1+reta2
umtr=reta1+reta3
dotr=reta2+reta3

if umdo>reta3 and umtr>reta2 and dotr>reta1:
    print('As retas formam um triângulo do tipo',end=' ')

    if reta1==reta2 and reta1==reta3 and reta2==reta3: #tambem podemos escrever:reta1==reta2==reta3 que VAI funcionar
        print('\033[31mEquilátero\033[m')

    elif reta1!=reta2 and reta1!=reta3 and reta2!=reta3: #tambem podemos escrever:reta1!=reta2!=reta3!=reta1 
        print('\033[33mEscaleno\033[m')

    else: 
        print('\033[36mIsósceles\033[m')
else: 
    print('As retas não são capazes de formar Triângulo')