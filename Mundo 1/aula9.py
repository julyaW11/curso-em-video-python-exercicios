frase='Curso em Vídeo Python'
#curso em video Python vai do caractere 0 ao 20
print(frase)

#Fragmentando Strings
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise de Strings
tam=len(frase)
con=frase.count('o')
ache=frase.find('deo')
ache0=frase.find('Peu')
dentro='Curso' in frase
print(tam)
print(con)
print(ache)
print(ache0)
print(dentro)

#Transformando Strings
frase2='Pepeto ReIs'
mai=frase2.title()
print(mai)

troca=frase.replace('Python','Android')
maius=frase.upper()
minus=frase.lower()
primeiramaius=frase.capitalize()
inuteis=frase.strip()
print(troca)
print(maius)
print(primeiramaius)
print(inuteis)

#Divisão de Stings
dividi=frase.split()
print(dividi)

#Juntando Strings
juntar=''.join(frase)
print(juntar)