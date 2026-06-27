nome=list() 
boletim=list()
mediageral=list()
nomess=list()
s='s'

while True:
    
    nome=str(input('Digite o nome do aluno: ')).strip()
    notaUm=float(input('Digite a 1° nota: '))
    notaDois=float(input('Digite a 2° nota: '))

    media=(notaUm+notaDois)/2
    
    boletim.append([nome,[notaUm,notaDois], media])

    
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
for i, c in enumerate(boletim):
    #i é a posição
    # c é o conteudo
    print(f'{i+1}     {c[0]}      {c[2]}')
 
        

while True:         
    posicao=int(input('\nIndique pelo número qual aluno você deseja rever a nota.(999 interrompe): '))



    if posicao==999:
        print('Consulta encerrada.')
        break
    
    else: 
        print('\nN°:     Nome:      Notas: \n')
        print(f'{posicao}       {boletim[posicao-1][0]}        {boletim[posicao-1][1]}')