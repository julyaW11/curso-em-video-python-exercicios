s=str(input('Diga se seu sexo é [M]asculino ou [F]eminino: ')).strip().upper() #[0]

while s!='F' and s!='M': #while s not in 'FfmM'
    print('\033[31mOpção Inválida!\033[m.Digite novamente: ')
    s=str(input('Diga se seu sexo é [M]asculino ou [F]eminino: ')).strip().upper()

print('Obrigada pela informação')