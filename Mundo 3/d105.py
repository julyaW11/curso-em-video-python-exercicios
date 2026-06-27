#Programa alternativo
def cadastro_alunos(*notas,sit=False):
    dicionario={}
    
    dicionario['total']=len(notas)
    dicionario['soma']=sum(notas)
    dicionario['maior']=max(notas)
    dicionario['menor']=min(notas)
    dicionario['media']=sum(notas)//len(notas) #soma//total
    
    media=dicionario['media']
    situation=''
    if sit==True:
        if media>7.0:
            situation='Ótima'
        elif media<=7.0 and media>4.99:
            situation='Razoável'
        else:
            situation='Preocupante'

        dicionario['situacao']=situation    
            
   
    return dicionario
#=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-==--=-==-=-=-=-==--===---==

#Programa principal:
resp=cadastro_alunos(8.5,6.5,9.5,10,sit=True)   
print()
print(resp)         
resp=cadastro_alunos(7.5,5.5,8.5,10)  
print(resp) 
    