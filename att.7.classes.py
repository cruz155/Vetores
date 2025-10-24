import os
os.system("cls")
from dataclasses import dataclass

@dataclass


class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    endereco: Endereco    



cliente1 = Cliente(nome="Marta",
                     endereco =Endereco
                    (logradouro="Rua A",
                     numero=23))

print("Mostrar dados cliente.")
print(f"nome: {cliente1.nome}") 
print(f"Endereco: {cliente1.endereco.logradouro}") 
print(f"Numero: {cliente1.endereco.numero}")