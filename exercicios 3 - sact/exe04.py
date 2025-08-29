# Script para verificar se uma letra é vogal, consoante ou inválida

# Solicita uma letra ao usuário
letra = input("Digite uma letra: ").strip().lower()

# Garante que seja apenas um caractere do alfabeto
if len(letra) != 1 or not letra.isalpha():
    print("Entrada inválida! Digite apenas uma letra do alfabeto.")
else:
    if letra in "aeiou":
        print(f"{letra.upper()} é uma Vogal.")
    else:
        print(f"{letra.upper()} é uma Consoante.")
