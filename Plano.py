import requests


def getPlano(user):
    url = "https://h4money.com/api/plano"
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def getPlanoById(user, id):
    url = "https://h4money.com/api/plano/" + str(id)
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
