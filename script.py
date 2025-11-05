import requests

res = requests.get('https://scotch.io')

print(res)

if res:
    print('resposta OK')
else:
    print('Resposta falhou')