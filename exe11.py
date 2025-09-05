# Entrada dos valores
cal1 = float(input("Digite o primeiro valor: "))
cal2 = float(input("Digite o segundo valor: "))

# Menu de operações
print("A - Adição")
print("S - Subtração")
print("M - Multiplicação")
print("D - Divisão")

# Escolha da operação
operacao = input("Digite qual operação deseja: ").strip().upper()

print("--------------------------------------------------------------")

# Estrutura de decisão
if operacao == "A":
    print("Resultado da adição:", cal1 + cal2)
elif operacao == "S":
    print("Resultado da subtração:", cal1 - cal2)
elif operacao == "M":
    print("Resultado da multiplicação:", cal1 * cal2)
elif operacao == "D":
    if cal2 != 0:  # evita divisão por zero
        print("Resultado da divisão:", cal1 / cal2)
    else:
        print("Erro: divisão por zero não é permitida!")
else:
    print("Opção inválida! Digite A, S, M ou D.")
