import os
os.system("cls")
from dataclass import dataclass


@dataclass
class Pessoa:
    nome : str
    Email : str
    Telefone : str
    Endereço : str


pessoa1 =Pessoa(input("digite seu nome"))
print(f"Nome:{pessoa1.nome}")
print(f"Email:{pessoa1.Email}")
print(f"Telefone:{pessoa1.Telefone} ")
print(f"Endereço:{pessoa1.Endereço} ")



