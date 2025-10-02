import os
os.system("cls")

# Criando um vetor.
lista_numeros = []

# Definindo constante com quantidade de números.
QUANTIDADE_NUMEROS = 2

print(f"Solicitando {QUANTIDADE_NUMEROS} números.")
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Digite uma número: "))
    # Inserindo uma número na lista de números.
    lista_numeros.append(numero)

# Verificando maior e menor números.
menor = min(lista_numeros)
maior = max(lista_numeros)

print("\nMostrando todas as números.")
for i in range(QUANTIDADE_NUMEROS):
    # O valor da variável i começa com zero.
    # O valor de i no vetor faz mostrar o índice no vetor.
    print(f"Número: {lista_numeros[i]}")

print(f"\nMenor número: {menor}")
print(f"Maior número: {maior}")