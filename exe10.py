# Script para calcular a média de três notas e dar feedback

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Arredondamento para 2 casas decimais
media = round(media, 2)

# Exibe a média
print(f"Sua média foi: {media}")

# Feedback baseado na média
if media >= 7.0:
    print("Parabéns! Sua média é alta.")
elif media >= 5.0:
    print("Sua média é razoável.")
else:
    print("Sua média é baixa. É uma boa oportunidade para melhorar.")
