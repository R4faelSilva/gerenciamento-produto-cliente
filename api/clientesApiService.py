import requests

# URL da api do json-server
url = "http://localhost:3000/clientes"

class ClienteApiService:
    # Fazendo a requisição GET
    def buscarClientes(self):
        response = requests.get(url)
        
        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print("Erro ao acessar a API:", response.status_code)

    # Buscar cliente no url tanto por id quanto por nome
    def buscarCliente(self, id=None, nome=None):
        if id and nome is not None:
            response = requests.get(f"{url}id={id}&nome={nome}")
        elif nome is not None:
            response = requests.get(f"{url}?nome={nome}")
        elif id is not None:
            response = requests.get(f"{url}/{id}")
        else:
            self.buscarClientes()
            return
    
    # Post sendo enviado o body JSON
    def adcionarCliente(self, nome):
        novo_cliente = {"nome": nome}
        response = requests.post(url, json=novo_cliente)

        if response.status_code == 201:
            print(f"{nome} foi adicionado a lista de clientes")
            return
        else:
            print("Erro ao adicionar o cliente:", response.status_code)
        
    # Put sendo enviado o body JSON
    def alterarCliente(self, id, nome):
        cliente_atualizado = {"nome": nome}

        response = requests.put(f"{url}/{id}", json=cliente_atualizado)

        if response.status_code == 200:
            print(f"{nome} foi atualizado a lista de clientes")
        else:
            print("Erro ao atualizar o cliente:", response.status_code)
    
    # Delete via parametro ID
    def removerCliente(self, id):
        response = requests.delete(f"{url}/{id}")

        if response.status_code == 200:
            print(f"Cliente de codigo {id} foi removido da lista de clientes")
        else:
            print("Erro ao remover o cliente:", response.status_code)


servico = ClienteApiService()
# clientes = servico.buscarCliente()
# servico.buscarCliente("1")
# servico.buscarCliente(None, "Joestar")
# servico.buscarCliente("f62e", "Joberson")
# servico.adcionarCliente("Joberson")
# servico.alterarCliente("1", "Joelson")
servico.removerCliente("3")