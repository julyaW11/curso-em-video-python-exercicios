from math import trunc, floor
n=float(input('De um numero:'))
print('A parte inteira do numero {} é {}\n'.format(n,floor(n)))

#usando a forma mais padrão, fazemos pelo trunch

n3=float(input('Digite um numero: '))
print('A parte inteira do numero {} é {}\n'.format(n3,trunc(n3)))

#tambem podemos fazer não usando a biblioteca math

n2=float(input('Digite um numero: '))
print('A parte inteira do numero {} é {}\n'.format(n2,int(n2)))

