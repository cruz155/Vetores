import os
os.system("cls")

# Texto que desejo salvar.
texto = "SENAI"
#definir nome do arquivo para salvar
nome_arquivo = "exemplo.txt"

#comando para salvar
with open(nome_arquivo, "w") as meu_arquivo:
    meu_arquivo.write(texto)
    print("salvo com sucesso!")

