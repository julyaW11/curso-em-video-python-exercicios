import os 
# ENTENDENDO FUNÇÕES:

# A função abaxo aceita receber DOIS parametros, ela irá somalos e printar.
print('\033[1m-=--=-=-=-=-=--=-=-=-=-=-=-=INICIO:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
def funcao1(a,b):
    soma = a + b
    print(soma)
    
    
funcao1(4,10) # dois parametros
funcao1(3,6) #dois parametros
#funcao1(1) se eu tentar passar MENOS DE DOIS parametros para a função o código dara erro. Descomente a linha para testar.
#funcao1(2,4,5) se eu tentar passar MAIS DE DOIS parametros para a função o código dara erro. Descomente a linha para testar. 


print('\033[31m-=-\033[m'*40)
def funcao2(a,b):
    print(f'a={a} * b={b}')
    mul = a*b
    print(mul)

funcao2(5,3)
funcao2(b=5,a=3) # passando os parametros do jeito que foi feito até a agora o "a" receberá o 1° número, o "b" o 2° número e aassim
#sucessivamente. Ao fazer o que fiz na linha 19 eu FORÇO que o 1° número vá para o parametro "b" e o 2° número para "a".

#####################################################################################################################################
#Se precisarmos de uma função com parametros indefinidos temos um modo de contornar o problEMA através do método do DESEMPACOTAMENTO
############################################################################################################################

print('\033[32m-=-\033[m'*40)
def funcao3(*num): #Quando colocamos este "*" dentro de uma função significa que ela pode receber uma quantidade INDEFINIDA de parametros. 
    # quando fazemos deste modo os argumentos passados são jogados dentro de uma TUPLA
    print(num)
    s=0
    for c in num:
        s+=c
    print(f'Em {num} a soma dos elementos será {s}')
    print()
    
funcao3(4,5,6,7,8,0)
funcao3(1,2,3)


#Quando fazemos do jeito abaixo os numeros serão passados em forma de LISTA.
print('\033[33m-=-\033[m'*40)
def funcao4(nomeQualquer):
    pos=0
    while pos<len(nomeQualquer):
        nomeQualquer[pos]*=2 #estou multiplicando o numero por 2
        pos+=1

valores=[1,2,3,4,5,6] #lista
funcao4(valores)
valores=[1,2,3,0,0] #lista
funcao4(valores)

#Funções podem não receber parametro algum
print('\033[34m-=-\033[m'*40)
def funcao5():
    print('Função sem parâmetro')

funcao5()

