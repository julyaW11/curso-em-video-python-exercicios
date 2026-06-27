casa=float(input('Diga o valor da casa:R$ '))
comp=float(input('Digite o salário do comprador(ra):R$ '))
anos=int(input('Em quantos anos a casa será financiada?: '))

mes=anos*12
pmensal=casa/mes

trinta=(comp*30)/100

print('O valor da parcela mensal será de \033[36mR${:.3f}\033[m'.format(pmensal))

if trinta>pmensal or trinta==pmensal :
   print('\033[36mEmpréstimo Concedido\033[m')
else :
    print('\033[31mEmpréstimo Negado! \033[m')