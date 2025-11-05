import requests

res = requests.get('https://scotch.io')

print(res)

if res:
    print('resposta OK')
else:
    print('Resposta falhou')

print(res.headers)
print(res.text)

#rode usando python scripy.py no terminal