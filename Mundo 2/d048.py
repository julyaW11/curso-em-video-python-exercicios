print('\033[32m A SOMA dos números impares que são múltiplos de três entre 1 e 500 dá:\033[m',end=' ')
soma=0

for c in range(1,501):        #FAZEMOS TAMBÉM : for c in range (1,51,2):
    if c%2!=0 and c%3==0:      # if c%3==0     #para diminuir o tempo do processador                                                               
        soma+=c
print('\033[31m{}\033[m'.format(soma))