from datetime import date
nasc=int(input('Diga em que ano você nasceu: '))
ano=date.today().year

idade=ano-nasc

print('Aos {} anos'.format(idade))

if idade==18:
    print('Você deve se alistar no Serviço Militar')
elif idade<18:
    tempf=18-idade
    print('Falta(m) \033[34m{} ano(s)\033[m para você se alistar no Serviço Militar'.format(tempf))
else :
    tempp=idade-18
    print('\033[33mVocê já passou da época de alistar no serviço militar YUP!\033[m')

