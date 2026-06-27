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
    
    print(f'Preço analisado:     \tR${n}')
    print(f'Dobro do Preço:      \tR${dobro}')
    print(f'Metade do Preço:     \tR${metade}')
    print(f'{more}% de aumento:  \tR${total_aumento}')
    print(f'{less}% de redução:  \tR${total_reduçao}')
    print()
    
    return None
