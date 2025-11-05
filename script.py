import requests

res = requests.get('https://scotch.io')

print(res)

if res:
    print('resposta OK')
else:
    print('Resposta falhou')

##print(res.headers)
##int(res.text)



API_KEY = 'your yandex api key' 

url = 'https://translate.yandex.net/api.v1.5/tr.json/translate'
res = requests.get.(url)

#rode usando python scripy.py no terminal