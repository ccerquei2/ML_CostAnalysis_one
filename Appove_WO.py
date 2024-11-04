
from zeep import Client
from zeep import Settings
from zeep.wsse.username import UsernameToken
from zeep.transports import Transport
import requests


class ApproveWorkOrder:


    def ApproveOrderJDE(self, environment, order):

        # Configurar a sessão para ignorar a verificação SSL (se necessário)
        session = requests.Session()
        session.verify = False  # Desabilita a verificação SSL

        transport = Transport(session=session)

        if environment == 'PD':    # URL do WSDL
            wsdl = 'https://bssvsistemas.granado.com.br:9061/PD910/CustomContabilizaOrdens?wsdl'
        else:
            wsdl = 'https://weberp06.granado.com.br:9052/PY910/CustomContabilizaOrdens?wsdl'


        # Credenciais
        username = 'CCERQUEIRA'
        password = '241193'

        # Criar o cliente SOAP com autenticação WS-Security
        client = Client(wsdl=wsdl, wsse=UsernameToken(username, password), transport=transport)

        # Parâmetros da chamada
        chave_ordem = int(order)
        version = 'CGRA0001J'

        # Realizar a chamada ao serviço
        try:
            response = client.service.ContabilizaOrdens(ordem=chave_ordem, version=version)
            # print(response)
            return "Submissão de aprovação da ordem " + str(int(order)) + " foi finalizada com sucesso."

        except Exception as e:
            print(f"Ocorreu um erro: {e}")


