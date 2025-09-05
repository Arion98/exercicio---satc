salario = float(input("Digite seu salário:"))

if(salario < 1000):
    novoSalario = salario * 1.10
    print("Seu novo salário é:", novoSalario)
else:
    novoSalario =salario * 1.05
    print("Seu novo salário é:", novoSalario)
    