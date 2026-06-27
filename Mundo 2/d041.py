from datetime import date
nasc=int(input('Digite o ano de nascimento do atleta: '))
ano=date.today().year

idade=ano-nasc
print('Tendo {} anos de idade'.format(idade))
if idade<=9:
    print('O atleta pertence à categoria \033[36mMIRIM\033[m')
elif idade<=14: #podemos deixar assim também que não causa dano
    print('O atleta pertence à categoria \033[31mINFANTIL\033[m')
elif idade>14 and idade<=19:
    print('O atleta pertence à categoria \033[35mJUNIOR\033[m')
elif idade<=25:
    print('O atleta pertence à categoria \033[32mSÊNIOR\033[m')
else :
    print('O atleta pertence à categoria \033[37;41mMASTER\033[m')
