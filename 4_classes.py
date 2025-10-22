import os 
from dataclasses import dataclass
os.system("cls")

#estrutura de dados : classe 
@dataclass
class Pessoa:
    nome:str
    idade: int
    Cpf:str

class Pet:
    nome:str
    idade: int
    peso: float

 #Exemplo de uso de classes  
pessoa1 = Pessoa("Marta", 20)  
pet1 = Pet("Totó", 4)

print("Exibindo dados da pessoa. ")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\n")


print("Exibindo dados do Pet.")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\n")
