import requests
import pprint

urlCliente = "https://h4money.com/api/cliente"

def getCliente(user):
    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
            }
    response = requests.request("GET", urlCliente, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def getClienteById(user, id):
    url = urlCliente + "/" + str(id)
    
    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
              }
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

def createCliente(user):
    payload = """{
                \r\n"nome": "Nome do Cliente",
                \r\n"cpf_cnpj": "123.456.789-05",
                \r\n"ativo": "S",
                \r\n"ie": "12.12.12-12",
                \r\n"im": "12.12.12-12",
                \r\n"telefone": "(86) 9999-9999",
                \r\n"endereco": "Endereço do cliente",
                \r\n"numero": "18",
                \r\n"complemento": "Complento do endereço",
                \r\n"bairro": "Bairro do cliente",
                \r\n"cep": "64212-150",
                \r\n"cidade": "Cidade do cliente",
                \r\n"uf": "RJ",
                \r\n"email": "cliente@emaildocliente.com.br",
                \r\n"observacao": "Observações sobre o cliente",
                \r\n"id_integracao": null,
                \r\n"id_plano": 65,
                \r\n"id_centro_custo": 41
            }"""
    headers = {
                'Authorization': f'Basic {user.token}',
                'Content-Type': 'application/json'
            }
    response = requests.request("POST", urlCliente, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def updateCliente(user, id):
    url = urlCliente + "/" + str(id)

    payload = """{
                \r\n"nome": "Nome do Cliente2",
                \r\n"cpf_cnpj": "123.456.789-05",
                \r\n"ativo": "S",
                \r\n"ie": "12.12.12-12",
                \r\n"im": "12.12.12-12",
                \r\n"telefone": "(86) 9999-9999",
                \r\n"endereco": "Endereço do cliente",
                \r\n"numero": "18",
                \r\n"complemento": "Complento do endereço",
                \r\n"bairro": "Bairro do cliente",
                \r\n"cep": "64212-150",
                \r\n"cidade": "Cidade do cliente",
                \r\n"uf": "RJ",
                \r\n"email": "cliente@emaildocliente.com.br",
                \r\n"observacao": "Observações sobre o cliente",
                \r\n"id_integracao": null,
                \r\n"id_plano": 65,
                \r\n"id_centro_custo": 41
            }"""
    headers = {
                'Authorization': f'Basic {user.token}',
                'Content-Type': 'application/json'
            }
    response = requests.request("PUT", url, headers = headers, data = payload)
    print(response.text.encode('utf8'))

def deleteCliente(user, id):
    url = urlCliente + "/" + str(id)

    payload  = {}
    headers = {
                'Authorization': f'Basic {user.token}'
            }
    response = requests.request("DELETE", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))