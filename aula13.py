def calculadora():
    print("Calculadora Simples")
    print("Operações disponíveis:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    operacao = input("Escolha a operação (1/2/3/4): ")

    if operacao in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacao == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacao == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacao == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        except ValueError:
            print("Erro: Digite apenas números válidos.")
    else:
        print("Operação inválida.")

# Executar a calculadora
calculadora()
