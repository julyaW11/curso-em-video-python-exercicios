br='Palmeiras','REB BULL', 'Athletico PR', 'Atlético MG', 'Fortaleza','Bahia','Santos','Atlético GO','Ceará','Fluminense','Flamengo','Juventude','Corinthians','Internacional','América MG','São Paulo','Sport','Cuiabá','Chapecoense','Grêmio'

print(f'Os times do Brasilerirão série A são: \n{br}\n')

print('Os 5 primeiros são: ')
print(f'{br[:5]}')

print('\nOs 4 últimos times são: ')
print(f'{br[16:]}')

print('\nEm ORDEM ALFABÉTICA: ')
print(sorted(br))

print('\n')
for c in range(0,len(br)):
    
    if br[c]=='Chapecoense': 
        print(f'A Chapeconse está na {c+1}° do Campeonato Brasileiro\n')

    if br.count('Chapecoense')==0:
        print('A Chapecoense não está na série A este ano')
        
#Caso seja GARANTIDO que a Chapecoense está na série A
print(f'A Chapecoense está na index {br.index("Chapecoense")+1} posição\n\n') 

