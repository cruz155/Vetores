import os
os.system("cls")
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome : str
    email : str
    telefone : str
    endereço: str

    def mostrar_dados(self):
       
        print("\n== Exibindo dados ==")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")


pessoa1 = Pessoa(nome = input("digite seu nome"),
                 email=input("digite seu email"),
                 telefone = input("digite seu telefone"),
                 endereço=input("digite seu endereço"))

print("exibindo dado de usuario.")
print(f"nome:{pessoa1.nome}email:{pessoa1.email}telefone:{pessoa1.telefone}")
print(f"Nome:     {pessoa1.nome}")
print(f"E-mail:   {pessoa1.email}")
print(f"Telefone: {pessoa1.telefone}")
print(f"Endereço: {pessoa1.endereco}")








