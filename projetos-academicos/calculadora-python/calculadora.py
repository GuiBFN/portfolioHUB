def menu():
    print("\nCalculadora em Python")
    print("----------------------")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calcular(opcao, a, b):
    if opcao == 1:
        return a + b
    elif opcao == 2:
        return a - b
    elif opcao == 3:
        return a * b
    elif opcao == 4:
        if b == 0:
            return "Erro: divisão por zero."
        return a / b
    else:
        return "Opção inválida."

while True:
    menu()
    try:
        opcao = int(input("Escolha uma opção (1-5): "))
        if opcao == 5:
            print("Encerrando...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = calcular(opcao, num1, num2)
        print("Resultado:", resultado)
    except ValueError:
        print("Entrada inválida! Digite números válidos.")
