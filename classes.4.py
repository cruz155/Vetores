from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

def solicitar_idade(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")

print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("digite seu nome: "),
                        idade=int(input("Digite sua idade: ")))


pessoa2 = Pessoa(nome=input("Digite seu nome: "))
idade=int(input("Digite sua idade: "))

print("\nExibindo dados =")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()