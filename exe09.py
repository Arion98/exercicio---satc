nome = input("Digite seu nome:")
situacao = print("Digite T - Técnico, E - Engenheiro de Software, A - Analista Sistemas, P - Programador, W - Web-Designer, G - Gerente Projetos")
cargo = input("Digite seu cargo:").upper()
salario = float(input("digite seu salário:"))

print("-----------------------------------------------------------------------------------------")

if(cargo == "T"):
    print("Seu nome:",nome)
    print("Seu salário:",salario)
    input("Seu cargo é Técnico")
elif(cargo == "E"):
    print("Seu nome:",nome)
    print("Seu salário:",salario)
    input("Seu cargo é Engenheiro de Software")
elif(cargo == "A"):
    print("Seu nome:",nome)
    print("Seu salário:",salario)
    input("Seu cargo é Analista Sistemas")
elif(cargo == "P"):
    print("Seu nome:",nome)
    print("Seu salário:",salario)
    input("Seu cargo é Programador")
elif(cargo == "W"):
    print("Seu nome:",nome)
    print("Seu salário:",salario)
    input("Seu cargo é Web-Designer")
elif(cargo == "G"):
    print("Seu nome:",nome)
    print("Seu salário:",salario)
    input("Seu cargo é Gerente Projetos")
else:
    input("Dados inválidos digite novamente!")