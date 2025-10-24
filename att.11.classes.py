import os
os.system("cls")
from dataclasses import dataclass

@dataclass

class pessoa:
    nome : str
    idade : int
    peso : float
    altura : float

    def solicitar_dados(self):
        print(f"nome {self.nome}idade{self.idade}peso{self.peso}altura{self.altura}")


lista_de_pessoa = [] 

for i in range(4):
    dados_da_pessoa = pessoa(nome = input("digite seu nome")idade = input("digite sua idade")peso(peso = input("digite seu peso")altura =("digite sua altura"))


