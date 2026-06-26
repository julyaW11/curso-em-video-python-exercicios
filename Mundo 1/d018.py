from math import sin,cos,tan,radians
n = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(n))
cos = cos(radians(n))
tang = tan(radians(n))
print('O seno, cosseno e tangente do angulo {:.1f} sao,respectivamente,{:.2f} {:.2f} {:.2f}'.format(n,sen,cos,tang))
