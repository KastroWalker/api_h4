import requests
import json
import Banco
from user import Usuario

url = "https://h4money.com/api/session"

def login():
    payload = """{
               \r\n"login": "victor.dev@h4money.com.br",
               \r\n"password": "senha",
               \r\n"keydev": ""
           }"""
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload).json()
    # print(response.text.encode('utf8'))
    id_user = response['usuario']['id']
    nome = response['usuario']['nome']
    login = response['usuario']['login']
    id_empresa = response['usuario']['empresas'][0]['id_empresa']
    nome_empresa = response['usuario']['empresas'][0]['nome_empresa']
    token = response['token'] 
    
    user = Usuario(id_user, nome, login, id_empresa, nome_empresa, token)

    return user

def getEmpresa(user):
    payload = """{
            \r\n"id_empresa":"%s",
            \r\n"id_usuario":"%s"
        }""" %(user.id_empresa, user.id_user)

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data = payload).json()
    # print(response)
    # print(response.text.encode('utf8'))
    user.token = response['token']

def main():
    user = login()
    getEmpresa(user)

    # BANCO
    # Banco.getBanco(user)
    # Banco.getBancoById(user, 153)
    # Banco.createBanco(user)
    # Banco.updateBanco(user, 334)
    # Banco.deleteBanco(user, 333)
    # Banco.getSaldo(user)
    # Banco.getBacen(user)
    Banco.getBacenById(user, 757)

main()
