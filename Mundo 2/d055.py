maior=0
menor=0

for c in range(1,6):
    peso=float(input('\033[33mDigite o peso da {}° pessoa Kg:\033[m '.format(c)))

    if c==1:
        maior=peso
        menor=peso

    else:
        if peso>maior:
            maior=peso
        
        if peso<menor:
            menor=peso
        
print('A pessoa de maior peso possui {}Kg e a de menor peso possui {}Kg'.format(maior, menor))