ficha={}

ficha['nome']=str(input('Digite o nome do(a) aluno(a): ')).strip()
ficha['media']=float(input('Digite a média: '))

print(f'O nome do(a) aluno(a) é \033[31m{ficha["nome"]}\033[m')
print(f'A média é \033[36m{ficha["media"]}\033[m')

 
if ficha['media']>=7:
    print('O(A) aluno(a) está APROVADO(A)')

elif 4<=ficha['media']<7:
    print('O(A) aluno(a) está de RECUPERAÇÃO')
    
else:
    print('O(A) aluno(a) está REPROVADO(A)')