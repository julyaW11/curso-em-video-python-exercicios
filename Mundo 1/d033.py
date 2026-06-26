pri=float(input('Digite o primeiro númeuro: '))
seg=float(input('Digite o segundo número: '))
ter=float(input('Digite o terceiro número: '))

if pri==seg and pri==ter and seg==ter:
    print('Os números são iguais')
if pri>seg and pri>ter :
    print('{:.1f} é o maior número e'.format(pri),end=' ')
if seg>pri and seg>ter :
    print('{:.1f} é o maior número e'.format(seg),end=' ')
if ter>pri and ter>seg :
    print('{:.1f} é o maior número e'.format(ter),end=' ')

if pri<seg and pri<ter:
     print('{:.1f} é o menor número'.format(pri))
if seg<pri and seg<ter:
      print('{:.1f} é o menor número'.format(seg))
if ter<pri and ter<seg:
      print('{:.1f} é o menor número\n'.format(ter))

#também podemos fazer assim:
print('-=-'*20)
print('PRÓXIMO RACIOCÍNIO')
print('-=-'*20)

pri1=float(input('Digite o primeiro númeuro: '))
seg2=float(input('Digite o segundo número: '))
ter3=float(input('Digite o terceiro número: '))

menor=pri1
if seg2<pri and seg2<ter3:
    menor = seg2
    print('{:.1f} é o menor número'.format(seg2))
if ter3<pri1 and ter3<seg2:
    menor=ter3
    print('{:.1f} é o menor número'.format(ter3))

maior=pri1
if seg2>pri1 and seg2>ter3:
    maior = seg2
    print('{:.1f} é o maior número'.format(seg2))
if ter3>pri1 and ter3>seg2:
    maior = ter3
    print('{:.1f} é o menor número'.format(ter3))
