from math import pow,sqrt,hypot
co = float(input('De o comprimento do Cateto Oposto: '))
ca = float(input('De o comprimento do Cateto Adjacente: '))
h = sqrt((pow(ca,2)+pow(co,2)))     # ainda podemos fazer: (ca**2 + co**2) *(1/2)
print('A hipotenusa mede {:.3f}\n'.format(h))

# e temos este jeitinho maroto de resolver que eu descobri por ACIDENTE

co1=float(input('De o comprimento do Cateto Oposto: '))
ca1=float(input('De o comprimento do Cateto Adjacente: '))
hi= hypot(co1,ca1)
print('A hipotenusa mede {:.2f}\n'.format(hi))