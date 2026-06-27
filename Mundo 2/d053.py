from time import sleep
#MÉTODO CLÁSSICO 
frase=str(input('Digite uma frase: ')).strip().upper() #VAMOS DESCONSIDERAR ACENTO

separa=frase.split() #separamos numa LISTA
junta=''.join(separa) #juntamos
inversa=''

for letra in range(len(junta)-1,-1,-1): #LEN COMEÇA A CONTAR A PARTIR DO 1
    inversa += junta[letra]
print('O inverso de {} é {}'.format(junta,inversa))

if inversa==junta:
    print('\033[36mTemos PALINDROMO!\033[m')
else:
    print('\033[31mA frase digitada NÃO forma PALINDROMO\033[m')

sleep(3)
#MÉTODO QUE SÓ FUNCIONA EM PYTHON:
frase1=str(input('Digite outra frase: ')).strip().upper()

separa1=frase1.split()
junta1=''.join(separa1)
inversa1=junta1[::-1]

print('O inverso de {} é {}'.format(junta1,inversa1))
if inversa1==junta1:
      print('\033[36mTemos PALINDROMO!\033[m')
else:
      print('\033[31mA frase digitada NÃO forma PALINDROMO\033[m')