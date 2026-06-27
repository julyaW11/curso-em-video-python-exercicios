from time import sleep 
n1=float(input('Digite o 1° número: '))
n2=float(input('Digite o 2° número: '))
a=0
sleep(1)
while a!=5:
    a=int(input(""" 
    [1]somar
    [2]subtrair
    [3]multiplicar
    [4]dividir
    [5]saia do programa

    \033[47;31mQual operação você deseja realizar?\033[m"""))
    print('\033[31mCarregando....\033[m')
    sleep(2)
    if a==1:
        print('\033[41mA soma entre \033[33m{} e \033[33m{} é \033[36m{}\033[m'.format(n1,n2,n1+n2))
    elif a==2:
        print('\033[41mA subtração entre \033[33m{} e \033[33m{} é \033[36m{}\033[m'.format(n1,n2,n1-n2))
    elif a==3:
        print('\033[41mA multiplicação entre \033[33m{} e \033[33m{} é \033[36m{}\033[m'.format(n1,n2,n1*n2))
    elif a==4:
        print('\033[41mA divisão entre \033[33m{} e \033[33m{} é \033[36m{}\033[m'.format(n1,n2,n1/n2))
    elif a==5: 
        print('\033[31mVocê saiu da operação, reinicie o programa caso deseje fazer novas operações!\033[m')
    else:
        print('\033[47;31mOpção inválida.Tente Novamente\033m')

