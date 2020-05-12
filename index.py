import requests
import json
import Banco
import Centro
import Cliente
import Fornecedor
import Lancamento
import Plano
import PlanoN1
import PlanoN2
import PlanoN2Tags
from user import Usuario

url = "https://h4money.com/api/session"


def login():
    payload = """{
               \r\n"login": "",
               \r\n"password": "",
               \r\n"keydev": ""
           }"""
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request(
        "POST", url, headers=headers, data=payload).json()
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
        }""" % (user.id_empresa, user.id_user)

    headers = {
        'Authorization': f'Basic {user.token}',
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "PUT", url, headers=headers, data=payload).json()
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
    # Banco.getBacenById(user, 757)

    # Centro de Custo
    # Centro.getCentro(user)
    # Centro.getCentroById(user, 135)
    # Centro.createCentro(user)
    # Centro.updateCentro(user, 232)
    # Centro.deleteCentro(user, 232)

    # Cliente
    # Cliente.getCliente(user)
    # Cliente.getClienteById(user, 124885)
    # Cliente.createCliente(user)
    # Cliente.updateCliente(user, 124885)
    # Cliente.deleteCliente(user, 124884)

    # Fonecedor
    # Fornecedor.getFornecedor(user)
    # Fornecedor.getFornecedorById(user, 2720)
    # Fornecedor.createFornecedor(user)
    # Fornecedor.updateFornecedor(user, 2720)
    # Fornecedor.deleteFornecedor(user, 2720)

    # Lancamento
    # Lancamento.getLancamento(user)
    # Lancamento.getLancamentoById(user, 64225)
    # Lancamento.createLancamento(user)
    # Lancamento.updateLancamento(user, 75951)
    # Lancamento.getReceberPagar(user, '2020-05-20')

    # Plano
    # Plano.getPlano(user)
    # Plano.getPlanoById(user, 3300189)

    # PlanoN1
    # PlanoN1.getPlanoN1(user)
    # PlanoN1.getPlanoN1ById(user, 330183)

    # PlanoN2
    # PlanoN2.getPlanoN2(user)
    # PlanoN2.getPlanoN2ById(user, 330012042)
    # PlanoN2.createPlanoN2(user)
    # PlanoN2.updatePlanoN2(user, 330012605)
    # PlanoN2.deletePlanoN2(user, 330012605)

    # PlanoN2Tags
    # PlanoN2Tags.getPlanoN2Tags(user)
    # PlanoN2Tags.getPlanoN2TagsById(user, 330012043)
    # PlanoN2Tags.createPlanoN2Tags(user)
    # PlanoN2Tags.updatePlanoN2Tags(user, 330012042)
    PlanoN2Tags.deletePlanoN2Tags(user, 330012042)

main()
