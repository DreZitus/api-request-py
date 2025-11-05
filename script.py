import requests

res = requests.get('https://scotch.io')

print(res)

if res:
    print('resposta OK')
else:
    print('Resposta falhou')

##print(res.headers)
int(res.text)


#pegando chave da API
API_KEY = 'your yandex api key' 

url = 'https://translate.yandex.net/api.v1.5/tr.json/translate'

#criação de dicionario com a função dict
params = dict(key=API_KEY, text='Hello', lang='en-es')

res = requests.get(url, params=params)

print(res.text)