valor=int(input('Quanto você quer sacar? R$'))

resulc=valor//50
porcin=valor-(resulc*50)

resulvin=porcin//20
porvin=porcin-(resulvin*20)

resuldez=porvin//10
pordez=porvin-(resuldez*10)

resulum=pordez//1

print('\n')
print('\033[36mVocê receberá: \033[m')
print('{} nota(s) de 50'.format(resulc))
print('{} nota(s) de 20'.format(resulvin))
print('{} nota(s) de 10'.format(resuldez))
print('{} nota(s) de 1'.format(resulum))





