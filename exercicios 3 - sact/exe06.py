nome = input("Digite seu nome:")
curso = input("Digite seu curso usando apenas uma sigla:").upper()   

if (curso == "ADM"):
    input("Seu curso é de administração")
elif(curso == "DIR"):
    input("Seu curso é de direito")
elif(curso == "CEX"):
    input("Seu curso é de comércio no exterior")
else:
    input("Sigla inválida digite novamente!")
