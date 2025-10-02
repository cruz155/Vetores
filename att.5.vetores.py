import os
os.system("cls")

numeros = []

# Leitura dos 6 números
for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Contagem de pares e ímpares
pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibição dos resultados
print("Números informados:", numeros)
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")                                                                                                                                                                                                                                                                                                                