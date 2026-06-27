pre=float(input('Digite o preço do produto:R$ '))
pag=str(input('Diga a forma de pagamento: ')).lower()

if pag=='dinheiro' or pag=='cheque' :
    desc=(pre*10)/100
    pref=pre-desc
    print('O produto custará \033[32mR${:.2f}\033[m'.format(pref))

if pag=='cartão':
    quantas=(input('Diga se será parcelado ou a vista no cartão: ')).lower()

    if quantas=='a vista':
        desc=(pre*5)/100
        pref=pre-desc
        print('O produto custará \033[32mR${:.2f}\033[m'.format(pref))

    elif quantas=='parcelado':
        vezes=int(input('Quantas vezes você deseja parcelar: ' ))

        if vezes<=2:
            pref=pre
            print('O produto custará \033[32mR${:.2f}\033[m'.format(pref))
        else :
            juros=(pre*30)/100
            pref=pre+juros
            print('O produto custará \033[32mR${:.2f}\033[m'.format(pref))

print('\033[47;36mObrgigada por escolher esta loja, volte sempre!\033[m')