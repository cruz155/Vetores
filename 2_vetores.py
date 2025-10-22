import os
os.system("cls")

def ler_nota(prompt):
    while True:
        try:
            valor = float(input(prompt).strip().replace(',', '.'))
        except ValueError:
            print("Entrada inválida. Digite um número entre 0 e 10.")
            continue
        if 0.0 <= valor <= 10.0:
            return valor
        print("Nota fora do intervalo. A nota deve ser entre 0 e 10.")

def calcular_media(n1, n2):
    return (n1 + n2) / 2.0

def aprovado(media, criterio=7.0):
    return media >= criterio

def main():
    print("Leitura de 2 notas do aluno (0 a 10).")
    nota1 = ler_nota("Digite a 1ª nota: ")
    nota2 = ler_nota("Digite a 2ª nota: ")
    media = calcular_media(nota1, nota2)
    print(f"Média: {media:.2f}")
    if aprovado(media):
        print("Resultado: APROVADO")
    else:
        print("Resultado: REPROVADO")

if __name__ == '__main__':
    main()
