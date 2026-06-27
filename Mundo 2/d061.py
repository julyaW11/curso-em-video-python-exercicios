num=int(input('Diga o 1° número da PA: '))
r=int(input('Diga a razão da PA: '))
#decimo= num + (10-1) * r  #isto aqui é uma FORMULA MATEMÁTICA para descobrir o décimo termo 


c=0
print('\033[34mOs 10 primeiros números da PA são: \033[m')

print('{}'.format(num),end=' ')
while(c!=9):
    nump=num+r
    print('{}'.format(nump),end=' ')
    num+=r
    c=c+1
    nump=0

#O NUM é o meu "c" rs 