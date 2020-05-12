import requests
import pprint

urlBanco = "https://h4money.com/api/banco"

def getBanco(user):
    payload = {}
    headers = {
            'Authorization': f'Basic {user.token}'
            }
    response = requests.request("GET", urlBanco, headers = headers, data = payload)
    #print(response.text.encode('utf8'))
    pprint.pprint(response.json())

def getBancoById(user, id):
    url = urlBanco + "/" + str(id)

    payload = {}
    headers = {
            'Authorization': f'Basic {user.token}'
            }   
    response = requests.request("GET", url, headers = headers, data = payload)
    #print(response.text.encode('utf8'))
    pprint.pprint(response.json())

def createBanco(user):
    payload = """{
                \r\n"apelido": "Itaú",
                \r\n"vl_saldo_inicial": 2320.75,
                \r\n"dt_inicio": "2019-01-01",
                \r\n"ativo": "S",
                \r\n"codigo_bacen": 341,
                \r\n"id_integracao": null
            }""".encode('utf-8')
    headers = {
            'Authorization': f'Basic {user.token}',
            'Content-Type': 'application/json'
            }
    response = requests.request("POST", urlBanco, headers = headers, data = payload)
    # print(response.text.encode('utf8'))
    pprint.pprint(response.json())

def updateBanco(user, id):
    url = urlBanco + "/" + str(id)

    payload = """{
                    \r\n"apelido": "Itaú2",
                    \r\n"vl_saldo_inicial": 2320.75,
                    \r\n"dt_inicio": "2019-01-01",
                    \r\n"ativo": "S",
                    \r\n"codigo_bacen": 341,
                    \r\n"id_integracao": null
               }""".encode('utf-8')
    headers = {
                'Authorization': f'Basic {user.token}',
                'Content-Type': 'application/json'
              }
    response = requests.request("PUT", url, headers = headers, data = payload)
    print(response.text.encode('utf8'))
    # pprint.pprint(response)

def deleteBanco(user, id):
    url = urlBanco + "/" + str(id)

    payload = {}
    headers = {
                'Authorization': f'Basic {user.token}'
              }
    response = requests.request("DELETE", url, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def getSaldo(user):
    url = "https://h4money.com/api/banco-total"
    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
              }
    response = requests.request("GET", url, headers = headers, data = payload)
    # print(response.text.encode('utf8'))
    pprint.pprint(response.json())

def getBacen(user):
    url = "https://h4money.com/api/bacen"
    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
              }
    response = requests.request("GET", url, headers=headers, data = payload)
    # print(response.text.encode('utf8'))
    pprint.pprint(response.json())

def getBacenById(user, id):
    url = "https://h4money.com/api/bacen/" + str(id)
    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
              }
    response = requests.request("GET", url, headers=headers, data = payload)
    # print(response.text.encode('utf8'))
    pprint.pprint(response.json())
