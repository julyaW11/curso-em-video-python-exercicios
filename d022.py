nome=input('Digite seu nome completo: ')
maior=nome.upper()
menor=nome.lower()
nesp=nome.count(' ')
tletras=len(nome)-nesp
dividi=nome.split()
pnome=len(dividi[0])
print(maior)
print(menor)
print('Este nome tem: {} letras'.format(tletras))
print('O primeiro nome é: {} e ele tem {} letras\n'.format(dividi[0],pnome))

print('TAMBEM PODEMOS CONTABILIZARA A QUANTIDADE DE LETRAS NO 1 NOME ASSIM:')
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))