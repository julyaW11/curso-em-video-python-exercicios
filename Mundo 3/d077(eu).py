palavras='aviao','roupa','oculos','piercing','sangue','grau','lanche'
acento=()
for c in range(0,len(palavras)):
    acento=palavras[c]
    print(f'\nNa palavra {acento.upper()} temos as vogais: ',end='')
    for c1 in range(0,len(acento)):

        if acento[c1] in 'Aa' or acento[c1] in 'Ee' or acento[c1] in 'Ii' or acento[c1] in 'Oo' or acento[c1] in 'Uu':
            print(f'{acento[c1]}',end=' ')

print('\n')