def resumo(n,more,less):
    print('-'*25)
    print(' '*4,end='')
    print('RESUMO DO PEDIDO',end='')
    print(' '*4)
    print('-'*25)
    
    metade=n/2
    dobro=n*2
    
    aumentou=(n*more)/100
    total_aumento=n+aumentou
    
    diminuiu=(n*less)/100
    total_reduçao= n - diminuiu
    
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
    print(f'Preço analisado     R${n}')
    print(f'Dobro do Preço      R${dobro}')
    print(f'Metade do Preço     R${metade}')
    print(f'{more}% de aumento     R${total_aumento}')
    print(f'{less}% de redução      R${total_reduçao}')
   
    
    return None
