import termoeda

n = float(input('Digite um preço: R$ '))
print(f'A metade de {termoeda.monetario(n)} é {termoeda.metade(n,False)}')
print(f'O dobro de {termoeda.monetario(n)} é {termoeda.dobro(n,True)}')
print(f'Ao aumentarmos o valor de {termoeda.monetario(n)} em 10% temos: {termoeda.aumenta(n,True)}')
print(f'Ao diminuirmos o valor de {termoeda.monetario(n)} em 13% temos: {termoeda.diminui(n,True)}')
