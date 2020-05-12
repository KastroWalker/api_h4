import requests
import pprint

urlCentro = "https://h4money.com/api/centro-custo"

def getCentro(user):
    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
            }
    response = requests.request("GET", urlCentro, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def getCentroById(user, id):
    url = urlCentro + "/" + str(id)
    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
            }
    response = requests.request("GET", url, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def createCentro(user):
    payload = """{
                \r\n"nome": "Escritorio",
                \r\n"ativo": "S",
                \r\n"id_integracao": null
            }"""
    headers = {
                'Authorization': f'Basic {user.token}',
                'Content-Type': 'application/json'
            }
    response = requests.request("POST", urlCentro, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def updateCentro(user, id):
    url = urlCentro + "/" + str(id)

    payload = """{
            \r\n"nome": "Escritorio2",
            \r\n"ativo": "S",
            \r\n"id_integracao": null
            }"""
    headers = {
                'Authorization': f'Basic {user.token}',
                'Content-Type': 'application/json'
            }
    response = requests.request("PUT", url, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def deleteCentro(user, id):
    url = urlCentro + "/" + str(id)

    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}',
            }
    response = requests.request("DELETE", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))