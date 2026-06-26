
frase=str(input('Digite uma frase:')).strip()
c=frase.upper().count('A')
ache=frase.upper().find('A')
acheR=frase.upper().rfind('A')
#Guanabara, eu te pego depois dessa.

print('O caractere A aparece {} vezes na frase '.format(c))
print('Primeiro aparece na posição {} e o ultimo na posição {}'.format(ache,acheR)) 
#print(ache)

