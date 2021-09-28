idade = int(input("Digite a sua idade: "))
anos = int(input("Digite quantos anos trabalhou: "))

if idade >= 65:
    print("Está qualificado.")
elif anos >= 30:
    print("Está qualificado.")
elif idade >= 60 and anos >= 25:
    print("Está qualificado")
else:
    print("Não está qualificado")
