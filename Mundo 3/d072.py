
while True: 
    nu=('zero','um','dois','tres','quatro','cinco,','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

    n=int(input('Digite um número entre 0 e 20: '))

    if n<0 or n>20 :
        while (n<0 or n>20): 
            n=int(input('Erro. Digite novamente um número entre 0 e 20: ')) 

            if n>=0 and n<=20 : 
                break

    ppe=len(nu) #pré pré extensp
    pe=n-ppe #pré extenso
    extenso=nu[pe]

    print(f'\nO número que você digitou foi o n° \033[31m{extenso}\033[m')
    print(f'{nu[n]}') #jeito fácil, jeito Guanabara. Como que eu não pensei nisso antes. 

    c=int(input("""\nDeseja continuar? \n1-SIM \n2-NÃO \n\nResposta: """))

    if c==2:
        break 


