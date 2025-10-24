import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.

# Cliente é uma pessoa?
# CPF? Endereço? Nome? Título de eleitor? E-mail? Telefone?
# Seu sistema precisa de algumas informações.
# Uma venda.
# Endereço, nome, telefone. (Mini-mundo)

@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str

    # Função apenas desta classe.
    def mostrar_dados_cliente(self):
        print(f"\nNome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}\n")


# Criando dois clientes com as características
# definidas na classe.

# Vetor.
lista_de_clientes = []

for i in range(3):
    dados_cliente = Cliente(nome=input("Digite seu nome: "),
                   endereco=input("Digite seu endereço: "),
                   telefone=input("Digite seu telefone: "))
    lista_de_clientes.append(dados_cliente)
    os.system("cls")

# Mostrando os dados do cliente.
for um_cliente in lista_de_clientes:
    # Posição: 0, 1, 2
    um_cliente.mostrar_dados_cliente()

Adicionar comentário para a turma...


Postada por Carlos Anderson Santos de Jesus
Carlos Anderson Santos de Jesus
Criado em: 13:3713:37
import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.
@dataclass
class Cliente:
    nome: str
    endereco: str


# Criando dois clientes com as características
# definidas na classe.
cliente1 = Cliente(nome="Marta", endereco="Rua A.")
cliente2 = Cliente(nome="João", endereco="Rua C.")

print("\n") # Deixando uma linha vazia.
print("Mostrando apenas os nomes dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Nome: {cliente2.nome}")

print("\n") # Deixando uma linha vazia.
print("Mostrando apenas os endereços dos clientes.")
print(f"Endereço: {cliente1.endereco}")
print(f"Endereço: {cliente2.endereco}")

print("\n") # Deixando uma linha vazia.
print("Mostrando todos os dados dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereco}\n")
print(f"Nome: {cliente2.nome}")
print(f"Endereço: {cliente2.endereco}\n")
     


