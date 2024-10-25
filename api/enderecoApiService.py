import http.client
import json

class EnderecoApiService:

    def consultarEnderecoIbge(self, cep=None):
        
        # Conectar ao servidor de API da Via Cep
        apiViaCep = http.client.HTTPSConnection("viacep.com.br")

        while True:
            # Solicitar o CEP ao usuário
            cep = input("Digite o CEP para consultar o enderço: ")

            # Enviar uma requisição GET
            apiViaCep.request("GET", f"/ws/{cep}/json/")

            # Obter a responsta
            response = apiViaCep.getresponse()

            data = response.read().decode("utf-8")
            endereco_json = json.loads(data)

            endereco_simples = {
                    "logradouro": endereco_json.get("logradouro"),
                    "bairro": endereco_json.get("bairro"),
                    "localidade": endereco_json.get("localidade"),
                    "uf": endereco_json.get("uf")
                }
            self.endereco = endereco_simples
            break

        return self.endereco


servico = EnderecoApiService()
servico.consultarEnderecoIbge()