genero = input("Digite seu gênero apenas F ou M:").upper()

if len(genero) != 1:
    print("Entrada inválida! Digite apenas um caractere.")
else:

 if(genero == "M"):
    input("Seu gênero é masculino")
 elif(genero == "F"):
    input("Seu genero é feminino")
 else:
    input("gênero inválido!")