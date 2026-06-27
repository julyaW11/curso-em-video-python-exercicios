print("-=-=-=-=-=-TUPLAS SÃO IMUTÁVEIS=--=-=-=-=-=\n")

a=(4,2,3,4,5)
b=(1,6,7,10)

c=a+b
d=b+a

print(c)
print(d)

print('\n\033[31mVimos que a+b !=  b+a\033[m')

print("\nA Função  INDEX ela diz em que POSIÇÃO esta determinado item da TUPLA\033[31m") 

print('O número 4 aparece 1° na posição: ')
print(c.index(4))
print(c.index(10))

print('\033[m\nAgora vamos ver a posição do n° 4 A PARTIR da posição 1')
print('INDEX NÃO INVALIDA NENHUMA POSIÇÃO\033[31m')
print('Considerando a partir do item 1 da tupla o n° 4 está na posição: ')
print(c.index(4,1))

print('\n\033[m-=--TUPLAS PODEM GUADAR \033[34m DIFERENTES TIPOS\033[m DE DADOS-=-=-=-')
Julia=('Júlia Maria',19,'Floripa','Peto','Tattos')

print(Julia)

print('\nPara deletar uma tupla eu faço: \033[31;47mDEL(tupla)\033[m')
del(Julia)
