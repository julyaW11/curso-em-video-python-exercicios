print('-=-=-=-=-=-=-=TUPLAS=-=-=-=-=-=-=-=-=\n') 

print('\033[34;47mTUPLAS SÃO IMUTÁVEIS\033[m\n')
almoço=('arroz','feijao','salada','costela','suco') #nao precisa de parenteses, coloquei no sentido didatico.


print(almoço)
print('\n\033[31;47mAgora vamos organizar a tupla no sentido ALFABÉTICO:\033[m\n')
print(sorted(almoço))

print('\n')
i=-5
for c in range (0,len(almoço),): 
    print(f'{almoço[c]}=={almoço[i]}')
    i+=1 



print('\n\033[31mCOMO VIMOS ACIMA:\033[m')
print("""O elemento que está em tupla[4] é o mesmo elemento que está na posição tupla[-1], então:
#tupla[3] == tupla[-2]
#tupla[2]== tupla[-3]
#tupla[1]== tupla[-4]
#tupla[0]== tupla[-5] \n""") 

print('\033[31mAs duas formas a seguir são equivalenetes:\033[m')


print('\n\033[33mFORMA TRADICONAL: Usamos quando queremos os elementos da tupla \033[m\n')
for c in almoço:
    print(f'Hoje eu almoçei {c}') 


print('\n\033[33mFORMA ALTERNATIVA: Usamos quando, além dos elementos, queremos saber suas POSIÇÕES dentro da tupla\033[m\n')
for c in range(0,len(almoço)): 
    print(f'Hoje no almoço teve {almoço[c]}')


print('\n\033[33mINVEnNÃO: Forma 2.0 de ter a POSIÇÃO dos elementos dentro da tupla \033[m\n')
for pos,c in enumerate(almoço):
    print(f'Hoje teve {pos}° {c} ,no almoço')
