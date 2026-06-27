from datetime import date

#Função
def voto(idade=0):
    
    ano=date.today().year
    anos=ano-idade
    
    print(f'Com {anos} ano(s):',end='')
    
    if anos>17 and anos<65:
        print(' VOTO OBRIGATÓRIO')
    
    elif anos<18:
        print(' NÃO VOTA')
    
    else:
        print(' VOTO OPICIONAL')
    
    print()
    return None

#Programa principal
vota=int(input('Digite o ano do seu nascimento: '))
voto(vota)