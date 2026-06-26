m=int(input('Digite em metros:'))
km=m/1000 
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000
print('{} metros equivale a:\n'.format(m)) 
print('{} quilometros'.format(km))
print('{} hectometros'.format(hm))
print('{} decametros'.format(dam))
print('{} centimetros'.format(cm))
print('e equivale á {} milimetros'.format(mm))