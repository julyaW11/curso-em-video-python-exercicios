palavras='aviao','roupa','oculos','piercing','sangue','grau','lanche'

for acento in  palavras:

    print(f'\nNa palavra {acento.upper()} temos as vogais: ',end='')
    for c1 in acento:
        if c1 in 'AaÁáãÃEeÊêIiÍíOoôÔõÕUuÚú':
            print(f'{c1}',end=' ')

print('\n')