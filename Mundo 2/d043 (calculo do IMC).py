alt=float(input('Digite aqui sua altura em metros: '))
peso=float(input('Digite aqui seu peso em Kg: '))

imc=peso/alt**2

print('\033[7mCom o IMC sendo {:.1f}\033[m'.format(imc))
if imc<18.5:
    print('Você está \033[33mabaixo\033[m do peso')

#TAMBÉM PODEMOS FAZER:

elif imc>=18.5 and imc<=25: # 18.5>= imc <=25  
    print('Você está no seu \033[36mpeso ideal\033[m, Parabéns!')

elif imc>25 and imc<=30: #25> imc <=30 
    print('Você está com \033[35;47msobrepeso\033[m')

elif imc>30 and imc<=40: # 30> imc <=40 
    print('Você está \033[35mobeso\033[m')

else:
    print('Você está com \033[1;31m obesidade mórbida\033[m,procure ajuda médica!')

#POUCAS LINGUAGENS DE PROGRAMAÇÃO ACEITAM ESTA FORMA DE COMPARAÇÃO 