###Nesta 1° SITUAÇÃO o sinal de IGUAL(=) entre a LISTA "a" e a LISTA "b" acaba criando uma conexão entre as listas, como resultado 
### uma operação que for feita em uma também se refletirá na outra. 
a=[2,3,4,7]
b=a

b[2]=0

print(f'Na LISTA A temos os números{a}.')
print(f'Na LISTA B temos os números{b}.')

print(15*'-=-')

#JÁ nesta 2° situação o que fazemos é o que DE FATO ESPERARÍAMOS no 1° procedimento, fazemos uma cópia da LISTA "c" para a LISTA "d". 
#assim a operação que fizermos em um NÃO se refletirá na outra. 
c=[2,3,4,7]
d=c[:]

d[2]=0

print(f'Na LISTA C temos os números{c}.')
print(f'Na LISTA D temos os números{d}.')