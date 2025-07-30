def analisar_numeros():
    pares = 0
    impares = 0

    print("Digite números inteiros. Digite 0 para encerrar.\n")

    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == 0:
                break
            elif numero % 2 == 0:
                print("→ Número par")
                pares += 1
            else:
                print("→ Número ímpar")
                impares += 1
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    print("\nAnálise final:")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Executar o programa
analisar_numeros()
