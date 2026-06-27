
#Programa alternativo
def funcao_help(istring=''):
    from time import sleep #Economiza memória
    
    sleep(1)
    print('',end='')#estética
    print('\033[34m~'*45)
    print(f'  Acessando o manual de comando {istring.upper()}')
    print('~'*45,end='')
    print('\033[m')#estética para agradar Guanabara.
    
    sleep(1)
    help(istring)
    print()#estética
    
#Programa Principal:
funcao=''
while funcao!='fim':
    print('\033[33m~'*25)
    print('Sistema de Ajuda PyHelp')
    print('~'*25,end='')
    print('\033[m')#estética para agradar Guanabara.
    
    funcao=input('Função ou Biblioteca> ')
    if funcao=='fim':
        break
    else:
        funcao_help(funcao)
    
   