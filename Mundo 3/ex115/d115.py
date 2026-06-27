def funcao_doc(*a):
    
    lista = [['Adalberta',73],['Jubiscleiton', 34],['Ricardo', 35], ['Caleb', 24], ['Pepeto', 6], ['Júlia', 23], ['Edon', 25]]
    for c in lista:
        
        tam=len(c[0])
        espaços = 20 - tam
        
        print(f'{c[0]}',end='')
        print(' '* espaços , end='')
        print(f'{c[1]}')
        
        
        
def cadastrar(*b):
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))

    nova_pessoa = [nome, idade]
    lista = ler_dados_do_arquivo()
    lista.append(nova_pessoa)

    escrever_dados_no_arquivo(lista)
    
def ler_dados_do_arquivo(*c):
    try:
        with open('pessoas.txt', 'r') as arquivo:
            lista = [linha.strip().split(',') for linha in arquivo]
            lista = [[nome, int(idade)] for nome, idade in lista]
        return lista
    except FileNotFoundError:
        return []

def escrever_dados_no_arquivo(lista):
    
    with open('pessoas.txt', 'w') as arquivo:
        for pessoa in lista:
            arquivo.write(f'{pessoa[0]},{pessoa[1]}\n')  
    print()


while True: 
    print()
    print('-'*35)
    print(' '*10,end='')
    print('MENU PRINCIPAL',end='')
    print(' '*10)
    print('-'*35) 

    print("""1 - Ver pessoas cadastradas
2 - Cadastrar Nova pessoa
3 - Sair do Sistema
      """)

    resposta = input('Sua Opção: ')

    if resposta == '1':
        funcao_doc()
    elif resposta == '2':
        cadastrar()
    elif resposta == '3':
        break
    else:
        print("Opção inválida! Por favor, escolha uma das opções válidas.")

print("Programa encerrado.")