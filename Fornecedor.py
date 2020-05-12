import requests

urlFornecedor = "https://h4money.com/api/fornecedor"


def getFornecedor(user):
    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request(
        "GET", urlFornecedor, headers = headers, data=payload)
    print(response.text.encode('utf8'))


def getFornecedorById(user, id):
    url = urlFornecedor + "/" + str(id)

    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request("GET", url, headers = headers, data=payload)
    print(response.text.encode('utf8'))


def createFornecedor(user):
    payload = """{
                    \r\n"nome": "Nome do Fornecedor",
                    \r\n"cpf_cnpj": "425.475.786-95",
                    \r\n"ativo": "S",
                    \r\n"ie": "95.85.45-47",
                    \r\n"im": "85.12.23-12",
                    \r\n"telefone": "(86) 8574-7584",
                    \r\n"endereco": "Endereço do fornecedor",
                    \r\n"numero": "45",
                    \r\n"complemento": "Complento do endereço",
                    \r\n"bairro": "Bairro do fornecedor",
                    \r\n"cep": "4458-457",
                    \r\n"cidade": "Cidade do fornecedor",
                    \r\n"uf": "RJ",
                    \r\n"email": "fornecedor@emaildofornecedor.com.br",
                    \r\n"observacao": "Observações sobre o fornecedor",
                    \r\n"id_integracao": null,
                    \r\n"id_plano": 65,
                    \r\n"id_centro_custo": 41
                }"""

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request(
        "POST", urlFornecedor, headers = headers, data=payload)
    print(response.text.encode('utf8'))


def updateFornecedor(user, id):
    url = urlFornecedor + "/" + str(id)

    payload = """{
                    \r\n"nome": "Nome do Fornecedor 2",
                    \r\n"cpf_cnpj": "425.475.786-95",
                    \r\n"ativo": "S",
                    \r\n"ie": "95.85.45-47",
                    \r\n"im": "85.12.23-12",
                    \r\n"telefone": "(86) 8574-7584",
                    \r\n"endereco": "Endereço do fornecedor",
                    \r\n"numero": "45",
                    \r\n"complemento": "Complento do endereço",
                    \r\n"bairro": "Bairro do fornecedor",
                    \r\n"cep": "4458-457",
                    \r\n"cidade": "Cidade do fornecedor",
                    \r\n"uf": "RJ",
                    \r\n"email": "fornecedor@emaildofornecedor.com.br",
                    \r\n"observacao": "Observações sobre o fornecedor",
                    \r\n"id_integracao": null,
                    \r\n"id_plano": 65,
                    \r\n"id_centro_custo": 41
                }"""

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }
    response = requests.request(
        "PUT", url, headers = headers, data=payload)
    print(response.text.encode('utf8'))


def deleteFornecedor(user, id):
    url = urlFornecedor + "/" + str(id)

    payload = {}
    headers = {
        'Authorization': f'Basic {user.token}'
    }
    response = requests.request(
        "DELETE", url, headers = headers, data=payload)
    print(response.text.encode('utf8'))
