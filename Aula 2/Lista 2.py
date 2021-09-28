#Exercício 1
n = 11
neg = 0


for i in range (1,n) :
 num = int (input("Digite o número " + str (i) + ": ")) 
 if num < 0 :
   neg = neg + 1

print ("O número de negativos é: " + str (neg))

#Exercício 2
n = 11
soma = 0

for i in range (1,n) :
 num = int (input("Digite o número " + str (i) + ": "))  
 soma = soma + num

media = soma / 10

print ("A soma destes números é: " + str (soma) + (" e a média é: " + str(media)))

#Exercício 3
n = 11
soma = 0

for i in range (1,n) :
 num = int (input("Digite o número " + str (i) + ": "))  
 if num < 40 :
  soma= soma + num
print ("A soma dos números inferiores a 40 é: " + str (soma))

#Exercício 4
soma = 0
quantidade = 0
for i in range(15, 101):
  print (i)
  soma = soma + i
  quantidade = quantidade + 1

media = soma / quantidade
print ("A soma dos números é: " + str (soma) + " e a média é de: " + str (media))

#Exercício 5
n = int(input ("Digite a quantidade de números que serão calculados: "))
soma = 0

for i in range (1,n+1) :
 num = int (input("Digite o número " + str (i) + ": "))  
 soma = soma + num

media = soma / n
media = round (media, 2)

print ("A média dos números é de: " + str (media))

#Exercício 6

n = 6
maior = 0
menor = 99999999999999
 
 
for i in range (1,n) :
 num = int (input("Digite o número " + str (i) + ": "))
 if num > maior :
  maior = num
 if num < menor :
   menor = num
 
print ("O maior número é: " + str (maior))
print ("O menor número é: " + str (menor))

#Exercício 7

a = 0
b = 1

n=6

for i in range (n) :
  print (b)
  aux = b
  b = b + a
  a = aux

#Exercício 8

n = 5

for i in range (2,n) :
  n = n*i
print (n)

fatorial = 1
n= 4
for i in range (n) :
  fatorial = fatorial * n
  n = n-1

print (fatorial)

#Exercício 9

def primo (x) :
  for i in range (2,x):
    if x % i == 0 :
      return False
    return True


n = int (input("Digite o valor de n: "))
x= 1

for i in range (n) :
  while not primo(x) :
    x = x+1
    print (x)
  x = x+1

  #Exercício 10

graos = 1
casas = 64
kilos = 0
km = 0
territorio_brasil = 0

graos = 2 ** 63
    
print(f"Quantidade de grãos necessários: {graos}")

kilos = graos / 170000

print("Quantidade de kilos: {}".format(round(kilos, 2)))

km = kilos / 550000

print("Quantidade de quilômetros necessários: {}".format(round(km, 2)))

territorio_brasil = km / 8514876

print("Quantidade de territórios brasileiros necessários: {}".format(round(territorio_brasil, 2)))

#Exercício 11

num=int(input('Tabuada do numero '))

for n in range (11):
  print(f'{num} x {n} = {num*n}')

#Exercício 12

nome = input("Digite o nome do produto: ")
qtd_adquirida = int(input("Digite a quantidade do produto: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = qtd_adquirida * preco_unitario

if qtd_adquirida <= 5:
    desconto = 0.02
elif qtd_adquirida > 5 and qtd_adquirida <= 10:
    desconto = 0.03
elif qtd_adquirida > 10:
    desconto = 0.05
     

print(f"Total antes do desconto: {total}")
print(f"Desconto de: {(total * desconto)}")
print(f"Total após do desconto: {total * (1 - desconto)}")

#Exercício 13

soma = 0
media = 0
conceito = ""

for x in range(3):
    nota = float(input(f"Digite a {(x + 1)}º nota: "))
    soma += nota
    
media = soma / 3

if media >= 9.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
elif media < 6.0:
    conceito = "D"
    
print(f"Conceito: {conceito}")

#Exercício 14

gasolina = float(input("Digite o valor do litro da gasolina: "))
alcool = float(input("Digite o valor do litro do álcool: "))

gasosa = gasolina * 0.7


if alcool <= gasosa:
    print("Alcool é mais vantajoso.")
    print(f"Preço do litro da gasolina: {gasolina}")
    print(f"Preço do litro do álcool: {alcool}")
else:
    print("Gasolina é mais vantojoso.")
    print(f"Preço do litro da gasolina: {gasolina}")
    print(f"Preço do litro do álcool: {alcool}")

#Exercício 15

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