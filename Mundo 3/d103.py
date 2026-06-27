#Função
def dados(nome='',gols=''):
    
    if nome!='' and gols!='':
        print(f'O(A) jogador(a) {nome} fez {gols} gols no campeonato.')
    
    elif nome!='' and gols=='':
        gols=0
        print(f'O(A) jogador(a) {nome} fez {gols} gols no campeonato.')
    
    elif nome=='' and gols!='':
        print(f'O(A) jogador(a) <desconhecido(a)> fez {gols} gols no campeonato.')
        
    else: 
        print(f'O(A) jogador(a) <desconhecido(a)> fez 0 gols no campeonato.')
        
    return None


#Programa principal 06,27:
nome=str(input('Digite o nome do(a) jogador(a): '))
gols=str(input('Digite quantos gols tal jogador(a) marcou: '))
print()
dados(nome,gols)

# def ficha(jogador='<desconhecido>', gol=0):
#     print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')

# #Programa principal
# nome=str(input('Nome do jogador: '))   
# goal=str(input('Número de gols: '))

# if goal.isnumeric():
#     goal=int(goal)
# else:
#     goal=0

# if nome.strip()=='':
#     ficha(gol=goal) #passa apenas 1 parâmetro

# else:
#     ficha(nome,goal)