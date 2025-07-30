def verificar_senha():
    senha = input("Digite sua senha: ")

    # Critério A: tamanho mínimo
    comprimento_ok = len(senha) >= 8

    # Critério B: contém pelo menos um número
    contem_numero = any(char.isdigit() for char in senha)

    # Verificação final
    if comprimento_ok and contem_numero:
        print("✅ Senha válida!")
    else:
        print("❌ Senha inválida. Motivos:")
        if not comprimento_ok:
            print("- Deve ter pelo menos 8 caracteres.")
        if not contem_numero:
            print("- Deve conter pelo menos um número.")

# Executar o verificador
verificar_senha()
