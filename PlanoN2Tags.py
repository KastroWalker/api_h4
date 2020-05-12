import requests

urlPlanoN2Tags = "https://h4money.com/api/planon2-tags"


def getPlanoN2Tags(user):
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request(
        "GET", urlPlanoN2Tags, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def getPlanoN2TagsById(user, id):
    url = urlPlanoN2Tags + "/" + str(id)

    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def createPlanoN2Tags(user):
    payload = """{
                \r\n"nome": "Nome da tag",
                \r\n"id_plano_n2": 330012042
                }"""

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request(
        "POST", urlPlanoN2Tags, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def updatePlanoN2Tags(user, id):
    url = urlPlanoN2Tags + "/" + str(id)

    payload = """{
                \r\n"nome": "Alteração do nome da tag 2",
                \r\n"id_plano_n2": 330012042
                }"""

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def deletePlanoN2Tags(user, id):
    url = urlPlanoN2Tags + "/" + str(id)

    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
