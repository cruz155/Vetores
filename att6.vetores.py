cardapio = [
    [1, "Picanha", 25.00],
    [2, "Lasanha", 20.00],
    [3, "Strogonoff", 18.00],
    [4, "Bife Acebolado", 15.00],
    [5, "Pão com ovo", 5.00]
]
# Lista com os pratos do cardápio. Cada prato é uma lista com: [código, nome, valor]

pedidos = []
# Lista para guardar os pratos escolhidos pelo usuário

continuar = 's'
# Variável de controle para o loop, começa como 's' (sim)
while continuar == 's':
    # Mostra o cardápio formatado
    print("CÓDIGO | PRATO           | VALOR (R$)")
    print("--------------------------------------")
    for prato in cardapio:
        print(f"{prato[0]:<7} | {prato[1]:<15} | {prato[2]:>7.2f}")
    
    codigo = int(input("Escolha o código do prato desejado: "))
    # Pede para o usuário digitar o código do prato

    match codigo:
        case 1:
            pedidos.append(cardapio[0])
            print(f"Você escolheu: {cardapio[0][1]} - R$ {cardapio[0][2]:.2f}")
        case 2:
            pedidos.append(cardapio[1])
            print(f"Você escolheu: {cardapio[1][1]} - R$ {cardapio[1][2]:.2f}")
        case 3:
            pedidos.append(cardapio[2])
            print(f"Você escolheu: {cardapio[2][1]} - R$ {cardapio[2][2]:.2f}")
        case 4:
            pedidos.append(cardapio[3])
            print(f"Você escolheu: {cardapio[3][1]} - R$ {cardapio[3][2]:.2f}")
        case 5:
            pedidos.append(cardapio[4])
            print(f"Você escolheu: {cardapio[4][1]} - R$ {cardapio[4][2]:.2f}")
        case _:
            print("Código inválido. Tente novamente.")
            continue
    # Usando match case, verifica qual prato foi escolhido e adiciona à lista de pedidos.
    # Se o código não existir, mostra mensagem de erro e volta para o início do loop.

    continuar = input("Deseja escolher outro prato? (s/n): ").strip().lower()
    # Pergunta se o usuário quer pedir mais pratos

print("\nPratos escolhidos:")
total = 0
for prato in pedidos:
    print(f"{prato[1]} - R$ {prato[2]:.2f}")
    total += prato[2]
# Mostra todos os pratos escolhidos e soma o valor total

print(f"Total a pagar: R$ {total:.2f}")
# Exibe o valor total da conta