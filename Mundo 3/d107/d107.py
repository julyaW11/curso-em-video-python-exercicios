import moeda

n=float(input('Digite um preço: R$ '))
print(f'A metade de {n:.0f} é {moeda.metade(n)}')
print(f'O dobro de {n:.0f} é {moeda.dobro(n)}')
print(f'Ao aumentarmos o valor de {n:.0f} em 10% temos: {moeda.aumenta(n)}')
print(f'Ao diminuirmos o valor de {n:.0f} em 13% temos: {moeda.diminui(n)}')
print()