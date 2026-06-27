from time import sleep
nu=[]
posiçao = [] *5 #PREDEFININDO TAMANHO DA LISTA

for c in range(0,5):
    nu.append(int(input(f"Digite o {c+1} número: ")))
    
#maior = max(nu)
#menor = min(nu)
print(nu)
print('=-=-=-=-=-=-=-')
sleep(3)

for c, valor in enumerate(nu): 
    posiçao[2] = valor[0]
    print(posiçao[2])
    sleep(5)
    mai = valor
    
    if valor[0] > mai:
        posiçao[[mai[c]+1]] = valor[0]
        mai = valor[0]
        
    else :
        posiçao[[mai[c]-1]] = valor[c]


print(posiçao)
    