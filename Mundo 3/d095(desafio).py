ficha_jogador=dict() #{}
nomeL=list()
n_partidasL=list()
soma_golsL=list()
gols_no_jogo=list()
s='s'
cont=0
#=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

while True: 
    nome=str(input('Digite o nome do(a) jogador(a): ')).strip()
    nomeL.append(nome)
    n_partidas=int(input(f'Digite quando partidas -{nome}- participou: '))
    n_partidasL.append(n_partidas)
    cont+=1
    c=0
    n_gols=0
    soma_gols=0
    l_gols=list()

    for c in range(0,n_partidas):
        n_gols=int(input(f'Diga quantos gols o(a) jogador(a) fez na {c+1}º partida: '))
        l_gols.append(n_gols)
        soma_gols+=n_gols
        
    soma_golsL.append(soma_gols)
    gols_no_jogo.append(l_gols)
    
    s=str(input('Deseja continuar?[Ss/Nn]: ')).lower()
    print()
    
    if s!='s':
        break 
    
    
#=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
ficha_jogador={'nome':nomeL,
       'total_gols': soma_golsL,
       'gols_jogos': gols_no_jogo
}
i=0
print('-=-'*20)
print('Nº:  Nome:       Gols         Total:')
for i in range(0,cont):
    print(f'{i+1}    {ficha_jogador["nome"][i]}    {ficha_jogador["gols_jogos"][i]}        {ficha_jogador["total_gols"][i]}')
print('-=-'*20)

#=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
while True: 
    numeroJ=int(input('Digite o n° do(a) jogador(a) você deseja rever os dados (999 interrompe): '))

    if numeroJ==999:
        break
    
    elif numeroJ>cont or numeroJ<=0:
        print('Este jogador não existe. Programa encerrado pois não tenho tempo pra palhaço. PASSAR BEM!')
        break 

    else:
        print(f'\033[31mDados do(a) jogador(a) {ficha_jogador["nome"][numeroJ-1]}:\033[m ')

        for i in range(0,len(gols_no_jogo[numeroJ-1])   ):
            print(f'No {i+1}° jogo fez: {ficha_jogador["gols_jogos"][numeroJ-1][i]} gol(s)')
        print(f'No total fez: {ficha_jogador["total_gols"][numeroJ-1]} gol(s)')
        print('\033[31m-=-=-=\033[m'*17)
        
print('\033[36mVolte sempre\033m\n')