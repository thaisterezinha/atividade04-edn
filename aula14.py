def calcular_media_turma():
    notas = []
    quantidade = int(input("Quantos alunos tem na turma? "))

    for i in range(quantidade):
        while True:
            try:
                nota = float(input(f"Digite a nota do aluno {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Digite um número válido.")

    media = sum(notas) / len(notas)

    print("\nNotas dos alunos:")
    for i, nota in enumerate(notas, start=1):
        print(f"Aluno {i}: {nota}")

    print(f"\nMédia da turma: {media:.2f}")

# Executar o programa
calcular_media_turma()
