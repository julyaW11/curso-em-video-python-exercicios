# 0-1-1-2-3-5
    #t1 t2 t3

print('\033[33m-=-\033[33m'*10)
print('\033[36mSequência de Fibonacci: \033[m')
print('\033[33m-=-\033[m'*10)

qt=int(input('Diga quantos termos da Sequência de Fibonacci você desja ver: '))

t1=0
t2=1
t3=0
c=3

print('{}-{}'.format(t1,t2),end='-')

while(c<=qt):
    t3=t1+t2
    print('{}'.format(t3),end='-')
    t1=t2
    t2=t3
    c+=1
print('FIM')