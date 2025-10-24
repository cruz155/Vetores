import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    Nome : str
    cpf: str
    telefone : str

    def mostrar_dados(self):
        print(f"nome{self.nome}cpf:{self.cpf}telefone:{self.telefone}")
    
    def dados_sms_marketing(self):
        print(F"telefone:{self.telefone}")

lista_de_pessoas = []
for i in range(3):

    dados_de_Pessoas_da_pessoa = Pessoa(nome=input("Digite seu nome: "),
                   cpf=input("Digite seu cpf: "),
                   telefone=input("Digite seu telefone: "))
    lista_de_pessoas.append(lista_de_pessoas)





for pessoas in lista_de_pessoas:
    pessoas.mostrar_dados()           
