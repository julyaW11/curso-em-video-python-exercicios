from random import randint 

sorteio=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(f'\033[7mOs números sorteados foram: {sorteio}\033[m')

for c in range(0,len(sorteio)):

    menor=sorteio[0]
    

    if sorteio[c]<menor:
        menor=sorteio[c]


    maior=sorteio[0]

    if sorteio[c]>maior:
        maior=sorteio[c]
    

print(f'\n0 \033[34mMENOR\033[m número dentre os sorteados é o n° \033[34m{menor}\033[m')
print(f'O \033[31mMAIOR\033[m número dentre os sorteados é o n° \033[31m{maior}\033[m\n')

print('\n\nPODEMOS USAR UMA FUNCIONALIDADE QUE EXISTE NA TUPLA max E min: ')

print(f'\n0 \033[34mMENOR\033[m número dentre os sorteados é o n° \033[34m{min(sorteio)}\033[m')
print(f'O \033[31mMAIOR\033[m número dentre os sorteados é o n° \033[31m{max(sorteio)}\033[m\n')


