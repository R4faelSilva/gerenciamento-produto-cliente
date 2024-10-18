import base64
from cryptography.fernet import Fernet # (pip install cryptography)
key = Fernet.generate_key()
fernet = Fernet(key)

usuarioLogin = "admin"
senhaLogin = fernet.encrypt('123'.encode())


# enctex = fernet.encrypt(senhaLogin.encode())
# dectex = fernet.decrypt(enctex).decode()

class Autenticacao:

  def autenticar(self, usuario, senha):
    if usuario == usuarioLogin and senha == fernet.decrypt(senhaLogin).decode():
      print("Acesso permitido!")
      return True
    else:
      print("Acesso negado!")
      return False