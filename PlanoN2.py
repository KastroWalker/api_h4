import requests

urlPlanoN2 = "https://h4money.com/api/planon2"


def getPlanoN2(user):
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request(
        "GET", urlPlanoN2, headers = headers, data=payload)
    print(response.text.encode('utf8'))


def getPlanoN2ById(user, id):
    url = urlPlanoN2 + "/" + str(id)
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers = headers, data=payload)
    print(response.text.encode('utf8'))


def createPlanoN2(user):
    payload = """{
                \r\n"nome": "Nome do palno de conta nivel 2",
                \r\n"id_plano": 3300189,
                \r\n"id_plano_n1": 330183,
                \r\n"ativo": "S"
            }"""

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", urlPlanoN2, headers = headers, data=payload)
    print(response.text.encode('utf8'))


def updatePlanoN2(user, id):
    url = urlPlanoN2 + "/" + str(id)

    payload = """{
                \r\n"nome": "Nome do palno de conta nivel 2 2",
                \r\n"id_plano": 3300189,
                \r\n"id_plano_n1": 330183,
                \r\n"ativo": "S"
            }"""

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request(
        "PUT", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def deletePlanoN2(user, id):
    url = urlPlanoN2 + "/" + str(id)

    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("DELETE", url, headers = headers, data=payload)
    print(response.text.encode('utf8'))
