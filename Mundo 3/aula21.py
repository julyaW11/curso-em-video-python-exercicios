# #DOC_STRING
# def funcao():
#     """
#     -Aqui está um DOCSTRING
#     Ele deve se encontrar logo atrás da função
#     """

#     print('Olá, mundo!')

# #Programa principal
# funcao()
# help(funcao)
# #=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# #PARÊMTRO OPCIONAIS

# def p_opcionais(a=0,b=0,c=0):
#     """
#     DOCSTRING:
#     Ao igualarmos "a","b" e "c" à ZERO , caso algum parâmetro não recebe um valor
#     o programa irá assumir que o valor do parâmentro será ZERO.
    
#     SE no lugar do ZERO fosse outro número 
#     aconteceria o mesmo fenômeno: caso algum parâmetro não recebesse um valor este número seria o valor deste parâmetro
#     """
#     print(f'"a" = {a}')
#     print(f'"b" = {b}')
#     print(f'"c" = {c}')
    
    
#     soma=a+b+c
#     print(f'A soma de "a" mais "b" mais "c" é {soma}')
#     print(10*'-=-')
#     print()
    
# p_opcionais(2,6,9)
# p_opcionais(1,2)
# p_opcionais(b=4,c=6)
# help(p_opcionais)

# #=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# #Escopo de Variáveis

# def escopo_variaveis():
    
#     a=8 #escopo local
#     b=4 #escopo local
#     c=2 #escopo local
#     soma=a+b+c
    
#     print(f'"a" = {a}')
#     print(f'"b" = {b}')
#     print(f'"c" = {c}')
    
    
#     print(f'SOMA: {soma}')
#     print()


# a=10#escopo global
# escopo_variaveis()
# print(f'"a" FORA da função = {a}')
# print()

# #Se eu fizer assim:

# def escopo_variaveis2():
#     global a2
#     a2=15 #escopo GLOBAL
#     b=4 #escopo local
#     c=2 #escopo local
#     soma=a2+b+c
    
#     print(f'"a" = {a2}')
#     print(f'"b" = {b}')
#     print(f'"c" = {c}')
    
    
#     print(f'SOMA: {soma}')
#     print()


# a2=5 
# escopo_variaveis2()
# print(f'"a" FORA da função = {a2}')
# #Como eu defini a2 como sendo uma variável global , a2 FORA da função perde seu valor 

# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
# #RETORNO DE FUNÇÕES

# def soma(a=0,b=0,c=0):
    
#     s=a+b+c
#     return s; 

# r1=soma(2,4,6)
# r2=soma(2,2)
# r3=soma(23)

# print(f'Os resultados foram, respectivamente, {r1}, {r2} e {r3}')
# #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=
# def par(n=0):
    
#     if n%2==0:
#         return True
#     else:
#         return False

# num=int(input('Digite um número inteiro: '))


# if par(num):
#     print('É par')
# else:
#     print('É impar')

#print(10==10)
num=input('Digite um número: ')

if num.isdigit():
  new=int(num)
  print(new)