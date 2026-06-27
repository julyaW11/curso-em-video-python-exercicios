ficha_jogador=dict() #{}

nome=str(input('Digite o nome do(a) jogador(a): ')).strip()
n_partidas=int(input(f'Digite quando partidas -{nome}- participou: '))

c=0
n_gols=0
soma_gols=0
l_gols=list()

for c in range(0,n_partidas):
    n_gols=int(input(f'Diga quantos gols o(a) jogador(a) fez na {c+1}º partida: '))
    l_gols.append(n_gols)
    soma_gols+=n_gols

ficha_jogador={'nome':nome,
       'total_gols': soma_gols,
       'gols_jogos': l_gols
}

print('--'*35)
print(ficha_jogador)
print('--'*35)

print(f'\033[36mNome:\033[m {ficha_jogador["nome"]}')
print(f'\033[36mGols em cada jogo:\033[m {ficha_jogador["gols_jogos"]}')
print(f'\033[36mTotal de Gols\033[m: {ficha_jogador["total_gols"]}')
print('-=-'*15)

for i, n in enumerate (ficha_jogador["gols_jogos"]):
    print(f'Na {i+1}º o(a) jogador(a) marcou: {n} gol(s)')

