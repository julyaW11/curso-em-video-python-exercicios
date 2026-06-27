from time import sleep
num=int(input('Digite um número inteiro: '))
sleep(1)

base1=int(input("""
[1] base Decimal
[2] base Binária
[3] base Octal 
[4] base Hexadecimal

Diga qual base está o número:  """))

base2=int(input("""
[1] base Decimal
[2] base Binária
[3] base Octal
[4] base Hexadecimal

Diga para qual base você deseja converter: """))

if base1==1 and base2==2:
    print('Convertido para Binário é {}'.format(bin(num)))

elif base1==1 and base2==3:
    print('Convertido para Octal fica {}'.format(oct(num)))

elif base1==1 and base2==4:
    print('convertido para Hexadecimal fica{}'.format(hex(num)))

#if base1==2 and base2==1 :
   