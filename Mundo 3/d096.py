def area(largura,altura):
    a=largura*altura
    print(f'A área do terreno de {largura} X {altura} terrno é {a:.2f} m².')


large=float(input('Digite a LARGURA do terreno em metros: '))
high=float(input('Digite a ALTURA do terreno em metros: '))

area(large,high)