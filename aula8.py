import math
num = int(input('De um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual à {:.4f}'.format(num,raiz))

#usando funcoes da biblioteca math, podemos arredondar raizes pra cima:

num1 = int(input('De mesmo numero de acima: '))
raiz1 = math.sqrt(num1)
print('A raiz de {} é igual à {}'.format(num,math.ceil(raiz1)))

# ou arredondamos para baixo

num2 = int(input('De o numero de antes: '))
raiz2 = math.sqrt(num2)
print('A raiz de {} é igual à {}'.format(num2,math.floor(raiz2)))