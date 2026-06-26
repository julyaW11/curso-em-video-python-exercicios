print('Olá, Caro cliente')
km=float(input('Diga quantos quilômetros terá sua viagem: '))

if km<=200:
    pas=km*0.50
    print('Sua passagem custará R${:.2f}'.format(pas))
else :
    pas=km*0.45
    print('Sua passagem custará R${:.2f}'.format(pas))

print('---BOA VIAGEM---\n') 

print('Também podemos resolver através do IF SIMPLIFICADO\n\n')

km1=float(input('Diga quantos quilômetros terá sua viagem: '))

pas1=km1*0.50 if km1<=200 else km1*0.45
print('Sua passagem custará R${:.2f}'.format(pas1))

print('---BOA VIAGEM---\n')


