a=int(input('Digite um numero:'))
b=int(input('Digite outro numero:'))
s=a+b
print('A soma entre {} e {} é {}'.format(a,b,s))
print(s.isnumeric())
print(s.isalpha())
print(s.isalnum())