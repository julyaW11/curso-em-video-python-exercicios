print('-=-'*20)

print('LOJA TEC ONLINE')

print('-=-'*20)

nbara=''
c=0
mcem=0
gastot=0 

while True: 
    nome=str(input('Nome do produto: ')).lower()
    pe=float(input('Preço do produto: R$ '))

    c+=1
    gastot+=pe 

    if c==1:
        br=pe
        nbara=nome

    elif c>1:
        if pe<br:
            br=pe
            nbara=nome

    if pe>1000:
        mcem+=1

    con=str(input('Deseja continuar sua compra? [S/N]: ')).upper()
    

    if con!='N' and con!='S':
        print('\033[31mRESPOSTA INVÁLIDA\033[m.Digite novamente')
        con=str(input('Deseja continuar sua compra? [S/N]: ')).upper()
        

    if con=='N':
        break


print('Você gastou no \033[33mtotal\033[m \033[36mR${:.2f}\033[m'.format(gastot))
print('\033[33m{}\033[m Produtos custaram mais que R$ 1000.00'.format(c))
print('\033[32m{}\033[m foi o produto mais barato'.format(nbara))