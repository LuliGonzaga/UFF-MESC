# Dados postais refente ao CEP:

import requests

def cep (n):
    
    url = 'http://viacep.com.br/ws/'+n+'/json/'
    dados = requests.get(url)
    return print (dados.json())


def cep2 (n):
    
    url = 'http://viacep.com.br/ws/'+n+'/json/'
    dados = requests.get(url)
    for chave, valor in dados.json().items():
        print(chave, ': ', valor)


cep(input('CEP: '))
#cep2(input('CEP: '))
