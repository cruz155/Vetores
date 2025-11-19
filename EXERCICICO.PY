import os 
os.system("cls")


from dataclasses import dataclass
@dataclass

class usario:
    nome : str
    data_nascimento : str
    rg : str
    cpf : str

def exibir_dado(self):
    print(f"nome:{self.nome} data_nascimento:{self.data_nascimento} rg:{self.rg} cpf: {self.cpf} ")


lista_de_usuarios = []
QUANTIDADE_DE_PESSOA = 5

for i in range(QUANTIDADE_DE_PESSOA):
    usario = usario(nome = input("digite seu nome: "),data_de_nascimento = input("digite sua data de nascimento:"),rg = input("digite seu rg"),cpf = input("digite seu cpf"))
    lista_de_usuarios.append(usuario)
    print()

nome_do_arquivo = "dados_paciente2.csv" 

with open(nome_do_arquivo,"a")
                     
