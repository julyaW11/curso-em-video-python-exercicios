import dmoeda

n = float(input('Digite um preço: R$ '))
print(f'A metade de {dmoeda.monetario(n)} é {dmoeda.monetario(dmoeda.metade(n))}')
print(f'O dobro de {dmoeda.monetario(n)} é {dmoeda.monetario(dmoeda.dobro(n))}')
print(f'Ao aumentarmos o valor de {dmoeda.monetario(n)} em 10% temos: {dmoeda.monetario(dmoeda.aumenta(n))}')
print(f'Ao diminuirmos o valor de {dmoeda.monetario(n)} em 13% temos: {dmoeda.monetario(dmoeda.diminui(n))}')
