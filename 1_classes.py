from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade:int

 #Exemplo de uso da classe
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob" , 25)

print(f"nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"nome: {pessoa2.nome}, Idade: {pessoa2.idade}")


