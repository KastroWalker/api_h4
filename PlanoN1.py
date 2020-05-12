import requests


def getPlanoN1(user):
    url = "https://h4money.com/api/planon1"
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def getPlanoN1ById(user, id):
    url = "https://h4money.com/api/planon1/" + str(id)
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
