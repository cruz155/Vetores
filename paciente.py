import os
os.system("cls")

from dataclasses import dataclass
class Paciente:
    idade:str
    nome:str

    def exibir_dados(self):
        print(f"nome:{self.nome} \nIdade:{self.idade}")

lista_de_pacientes = []
QUANTIDADES_DE_PACIENTES = 2

for i in range( QUANTIDADES_DE_PACIENTES):
    paciente = Paciente
        nome = input("digite seu nome: "),
         idade = int(input("digite sua idade: "))
    )
    lista_de_pacientes.append(paciente)    
    print() # pular uma linha

    nome_do_arquivo = "dados_paciente.csv"
    with open(nome_do_arquivo,"a")as arquivo_pacientes:
        for paciente in lista_de_pacientes
        arquivo_pacientes.whrite(f"{paciente.nome}, {paciente.idade}")
        print("dados salvos com sucesso")
 
        print("\nExibindo lista_de_pacientes")
        for paciente in lista_de_pacientes:
            paciente.exibir_dados()