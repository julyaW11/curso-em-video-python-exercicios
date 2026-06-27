nome=list() 
notaBruta=list()
notas=list()
mediageral=list()
nomess=list()
s='s'

while True:
    
    notaBruta=list() 
    
    nome=str(input('Digite o nome do aluno: ')).strip()
    notaUm=float(input('Digite a 1° nota: '))
    notaDois=float(input('Digite a 2° nota: '))

    media=(notaUm+notaDois)/2
    
    notaBruta.append(notaUm)
    notaBruta.append(notaDois)
    notas.append(notaBruta)
    
    del notaBruta
    
    nomess.append(nome)
    mediageral.append(media)
    
    s=str(input('Deseja continuar?[S/N]:'))
    
    if s in'Ss':
        continue
    
    else:
        break

c=0
posicao=0 
print('\n')
print('-=-=-=-=LISTA DE ALUNOS=-=-=-')

print('N°:        Nome:           Média\n')
for c in range(0,len(nomess)):
    print(f'{c+1}       {nomess[c]}    {mediageral[c]:.2f}')
        

while True:         
    posicao=int(input('\nIndique pelo número qual aluno você deseja rever a nota.(999 interrompe): '))



    if posicao==999:
        print('Consulta encerrada.')
        break
    
    else: 
        print('\nN°:     Nome:                              Notas: \n')
        print(f'{posicao}       {nomess[posicao-1]}        {notas[posicao-1]}')   
   






    
    