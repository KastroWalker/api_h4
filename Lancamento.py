import requests

urlLancamento = "https://h4money.com/api/lancamento"


def getLancamento(user):
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request(
        "GET", urlLancamento, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def getLancamentoById(user, id):
    url = urlLancamento + "/" + str(id)

    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def createLancamento(user):
    payload = """{
                \r\n"situacao": "p",
                \r\n"id_banco": 334,
                \r\n"dt": "2019-10-13",
                \r\n"descricao": "Descrição do lançamento",
                \r\n"vl": "1000.00",
                \r\n"id_plano": 1046,
                \r\n"tipo": "s",
                \r\n"id_cliente": null,
                \r\n"id_fornecedor": null,
                \r\n"id_centro_custo": 135,
                \r\n"id_usuario": 3,
                \r\n"observacao": "Observação do lançamento",
                \r\n"id_integracao": null,
                \r\n"ativo": "s",
                \r\n"dt_competencia": "2019-10-18"
                }"""
    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request(
        "POST", urlLancamento, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def updateLancamento(user, id):
    url = urlLancamento + "/" + str(id)

    payload = """{
                \r\n"situacao": "p",
                \r\n"id_banco": 334,
                \r\n"dt": "2019-10-13",
                \r\n"descricao": "Descrição do lançamento 2",
                \r\n"vl": "1000.00",
                \r\n"id_plano": 1046,
                \r\n"tipo": "s",
                \r\n"id_cliente": null,
                \r\n"id_fornecedor": null,
                \r\n"id_centro_custo": 135,
                \r\n"id_usuario": 3,
                \r\n"observacao": "Observação do lançamento",
                \r\n"id_integracao": null,
                \r\n"ativo": "s",
                \r\n"dt_competencia": "2019-10-18"
                }"""
    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))


def getReceberPagar(user, dt):
    url = urlLancamento + "/?dt=" + dt

    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))
