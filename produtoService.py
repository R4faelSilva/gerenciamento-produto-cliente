produtos = [
  {"id": 1, "descricao": "Prato"},
  {"id": 2, "descricao": "Caneca"},
  {"id": 3, "descricao": "Garfo"},
  {"id": 4, "descricao": "Faca"}
]

class Produto:
  TODOS = "TODOS"
  SAIR = "SAIR"

  def adicionarProduto(self):
    descricao = input("Qual o nome do produto que deseja adicionar? ")
    proximoId = len(produtos)+1
    while next((produto for produto in produtos if produto["id"] == proximoId), None) is not None:
      proximoId += 1
    produtos.append({"id": proximoId, "descricao": descricao})

    print(f"{descricao} foi adicionado a lista de produtos")


  def editarProduto(self):
    while True:
      id = input("Digite o código do produto que deseja editar ou digite 'Sair' para voltar ao menu: ")

      if(id.upper() == self.SAIR):
        break

      produto_encontrado = produto_encontrado = self.consultarProdutoPorId(id)

      if produto_encontrado is None:
          print("ID não encontrado. Veja a lista de produtos:")
          self.consultarProduto(self.TODOS)
          continue
      
      print(f"Dados atuais do produto: {produto_encontrado['id']} - {produto_encontrado['descricao']}")

      novo_nome = input("Digite o novo nome do produto: ")

      produto_encontrado['descricao'] = novo_nome

      print(f"Produto atualizado: {produto_encontrado['id']} - {produto_encontrado['descricao']}")
      break

  def removerProduto(self):
    while True:
      try:

        id = input("Digite o código do produto que deseja removerou digite 'Sair' para voltar ao menu: ")

        if(id.upper() == self.SAIR):
          break

        produto_encontrado = self.consultarProdutoPorId(id)

        if produto_encontrado is None:
          print("ID não encontrado ou ja removido. Veja a lista novamente.")
          self.consultarProduto(self.TODOS)
          return
        
        produtos.remove(produto_encontrado)

        print(f"Produto {produto_encontrado['descricao']} removido com sucesso!")
        break
      except TypeError:
        print("O id não esta na lista ou ja foi removido.")
        return
  def consultarProduto(self):

    id = input("Digite o id do produto que deseja buscar! (Digite 'todos' para retornar todos os produtos cadastrados) ")
    
    if isinstance(id, str) and id.upper() == "TODOS":
      for produto in produtos:  
        print(f"{produto['id']} - {produto['descricao']}")
    else:  
      produto = self.consultarProdutoPorId(id)
      print(f"Dados do produto: {produto['id']} - {produto['descricao']}")
    
  def consultarProdutoPorId(self, id):
    try:
        id = int(id)
    except ValueError:
      print("Não foi digitado um número inteiro!")
      return

    produto_encontrado = None

    for produto in produtos:
        if produto["id"] == id:
            produto_encontrado = produto
            break
      
    return produto_encontrado