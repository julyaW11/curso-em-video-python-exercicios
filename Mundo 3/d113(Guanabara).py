def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mVocê NÃO digitou um número inteiro.Tente novamente:\033[m')
            #continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário decdidu não digitar número.\033[m')
            return 0 
        else:
            return n 

def leiaFloat(msg):
    while True: 
        try:
            n=float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mVocê NÃO digitou um número inteiro.Tente novamente:\033[m')
            #continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário decdidu não digitar número.\033[m')
            return 0 
        else:
            return n 
    
 
 #Código Principal
numI = input('Digite um número: ') 
numI = leiaInt(numI)
print(f'Você digitou o número INTEIRO {numI}')
print(' ')
numF = input('Digite um número FLOAT: ')
numF = leiaFloat(numF)
print(f'Você digitou o número FLOAT {numF}')