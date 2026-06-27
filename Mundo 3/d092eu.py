from datetime import datetime 

banco=dict()
ano_atual=datetime.now().year

    
nome=str(input('Digite seu nome: ')).strip()
ano=int(input('Digite seu ano de nascimento: '))
ctps=int(input('Digite o número da sua Carteira de trabalho (0 não tem): '))

if ctps!=0:
    contratacao=int(input('Digite o ano da contratação: '))
    salario=int(input('Digite o salário: R$  '))
    
    banco={'nome':nome,
        'idade':ano_atual-ano,
        'CTPS':ctps,
        'ano_contratacao':contratacao,
        'salario':salario,
        'aposentadoria':(contratacao-ano)+35 ##tempo de contruição é de 35 anos                     
    }

else:
    banco={'nome':nome,
        'idade':ano_atual-ano,
        'CTPS':ctps                    
    }

print('--'*15)
print(banco)
print('--'*15)

if ctps!=0:
    print(f'\033[36mNome:\033[m {banco["nome"]}')
    print(f'\033[36mIdade:\033[m {banco["idade"]}')
    print(f'\033[36mCarteira de Trabalho:\033[m {banco["CTPS"]}')
    print(f'\033[36mAno de Contratação:\033[m {banco["ano_contratacao"]}')
    print(f'\033[36mSalário: \033[mR$ {banco["salario"]}')
    print(f'\033[36mIrá se aposentar com: \033[m{banco["aposentadoria"]} anos')

        
else:
    print(f'\033[36mNome:\033[m {banco["nome"]}')
    print(f'\033[36mIdade:\033[m {banco["idade"]}')
    print(f'\033[36mNão trabalha ainda\033[m') 

