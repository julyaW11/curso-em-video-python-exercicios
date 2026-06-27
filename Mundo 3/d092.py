from datetime import datetime 

banco=dict()
ano_atual=datetime.now().year

    
banco['nome']=str(input('Digite seu nome: ')).strip()
banco['ano']=int(input('Digite seu ano de nascimento: '))
banco['ctps']=int(input('Digite o número da sua Carteira de trabalho (0 não tem): '))

if banco['ctps']!=0:
    banco['contratacao']=int(input('Digite o ano da contratação: '))
    banco['salario']=float(input('Digite o valor do salário: R$ '))
    banco['aposentadoria']=(banco['contratacao']-banco['contratacao']) +35


for k , v in banco.items():
    print(f'{k}: {v}')