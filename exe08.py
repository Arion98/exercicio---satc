nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

if(idade >= 0 and idade <= 10 ):
    input("Sua categoria é infantil")
elif(idade >= 11 and idade <= 17):
    input("Sua categora é juvenil")
elif(idade >= 18 and idade < 30):
    input("Sua categoria é adulto")
elif(idade >= 30 and idade <= 60):
    input("Sua categoria é Sênior")