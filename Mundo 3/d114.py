import requests

url = 'http://www.pudim.com.br'
response = requests.get(url)

if response.status_code == 200:
     print(response.text)
     
else :
    print(f'Erro: \n{response.status_code}')
     