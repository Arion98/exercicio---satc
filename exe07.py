nome = input("Digite seu nome:")
situacao = print("Digite S - solteiro, C - casado, V - viúvo, D - divorciado")
estadoCivil = input("Digite seu estado civil:").upper()

if(estadoCivil == "S"):
    print("Seu nome:",nome)
    input("Seu estado civil é solteiro")
elif(estadoCivil == "C"):
    print("Seu nome:",nome)
    input("Seu estado civil é casado")
elif(estadoCivil == "V"):
    print("Seu nome:",nome)
    input("Seu estado civil é viúvo")
elif(estadoCivil == "D"):
    print("Seu nome:",nome)
    input("Seu estado civil é divorciado")
else:
    input("Dados inválidos digite novamente!")