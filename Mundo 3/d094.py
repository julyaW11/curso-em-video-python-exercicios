nomeL=list()
idadeL=list()
sexoL=list()
feminino=list()
cadastro={}
s='s'
cont=0

while True:
   
   nomev=str(input('Digite o nome: '))
   nomeL.append(nomev)
   idadeL.append(int(input('Digite a idade: ')))
   sx=str(input('Dê o sexo [F/M]: ')).lower()
   sexoL.append(sx)
   
   cont+=1
   
   if sx=='f':
       feminino.append(nomev)
       
       
   s=str(input('Deseja continuar?[S/N]: ')).lower()
   
   if s!='s':
    break
    
cadastro={'nome':nomeL,
         'idade':idadeL,
         'sexo':sexoL,
         'mulher':feminino  
}

soma=0
media=0
for c in cadastro["idade"]:
     soma+=c

media=soma/cont

print('\n')
print(f'\033[34mNúmero de pessoas cadastradas:\033[m {cont}')
print(f'\033[34mMédia de idade das pesssoas cadastradas:\033[m {media}')
print('\033[34mAs mulheres cadastradas foram:\033[m',end='')
for c in cadastro["mulher"]:
    print(f' {c}',end=' ')
    
print('\033[34mAs pessoas que possuem idade acima da idade são:\033[m ')

for i, c in enumerate(cadastro["idade"]):
    if c>media: 
        print(f'{cadastro["nome"][i]}, com {c} anos.')
        
        