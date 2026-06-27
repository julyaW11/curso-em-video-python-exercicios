import defteste
from pacote import numeros


while True:
    numero=int(input('Digite um número. Nosso programa irá fonever a tabuada dele.\nNúmero:'))
    
    if numero==0:
        print('Obrigada por usar nosso programa,volte sempre!')
        break
    else:
        n1=numero
        print(f'{defteste.tabuada(numero)}')
        print()
        
print(numeros.dobro(n1))
