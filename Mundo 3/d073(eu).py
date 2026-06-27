br='Palmeiras','REB BULL', 'Athletico PR', 'Atlético MG', 'Fortaleza','Bahia','Santos','Atlético GO','Ceará','Fluminense','Flamengo','Juventude','Corinthians','Internacional','América MG','São Paulo','Sport','Cuiabá','Chapecoense','Grêmio'

print('OS 5 primeiros colocados do Brasileirão são: \n')


for c in range (0,len(br[5])):

    i=br[c] 
    if (i!=br[4]):  
        print(f'{c+1}° {br[c]}',end=', ')

    else: 
         print(f'{c+1}° {br[c]}\n')





print('Os 4 últimos colocados são: \n')
for pos,c in enumerate (br[16:]): 

    f=br[pos]

    if f!=br[19]:
        print(f'{pos+17}° {c}',end=', ')
    
    else: 
        print(f'{pos+17}° {c} \n')

print('Os times em ORDEM ALFABÉTICA: \n')
print(sorted(br))
print('\n')


for c in range(0,len(br)):

    
    if br[c]=='Chapecoense': 
        print(f'A Chapeconse está na {c+1}° do Campeonato Brasileiro\n')

    if br.count('Chapecoense')==0:
        print('A Chapecoense não está na série A este ano')
    





