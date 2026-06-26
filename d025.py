nome=str(input('Digite seu nome completo:'))
nomeM=nome.upper()
existe='SILVA' in nomeM
print('Seu nome tem Silva? {}'.format(existe))

#já que nao sabemos onde vai aperecer o Silva, usamos IN
#tanto IN quanto UPPER/Lower printan TRUE/FALSE
