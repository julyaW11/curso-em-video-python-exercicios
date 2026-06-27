num=int(input('Diga o 1° número da PA: '))
r=int(input('Diga a razão da PA: '))
decimo= num + (10-1) * r  #isto aqui é uma FORMULA MATEMÁTICA para descobrir o décimo termo 

print('Os 10 primeiros números desta PA são: ')
for c in range(num,decimo+r,r):      #décimo + razão 
    print(c ,end=' ')
