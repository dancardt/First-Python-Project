numeros = [18,19,21]
nomes = ["Joao", "Maria", "Pedro"]

for i in range (len(numeros)) :
  numero = numeros[i]
  print (numero)

for i in range (len(nomes)) :
  nome = nomes[i]
  print (nome)

print ("_____________")

for i in range (len(numeros)) :
  numero = numeros[i]
  nome = nomes [i]
  print (f"Nome: {nome}, Idade: {numero}")

#------------------------------------------
  numeros = [2,5]

print (len(numeros))

numeros.append(10)
numeros.append(20)
numeros.append(30)

print (len(numeros))

for numero in numeros:
  print (numero)

#Lista com Input
numeros = []

for numero in range (3):
  numero = int (input("Digite um número: "))
  numeros.append(numero)


for numero in numeros:
  print(numero)

#ista com input 2

numeros = []
n = int(input("Digite n: "))

for i in range (n):
  numero = int (input("Digite um número: "))
  numeros.append(numero)


soma = 0
for numero in numeros:
  soma = soma+ numero


for numero in numeros:
  print(numero)


print (f"O somatorio foi: {soma}")

#ALTERANDO O ARRAY
numeros = [10,20,30]

print(numeros[0])

numeros [0] = 15

print(numeros[0])

#INVERTENDO O ARRAY
numeros = [10,20]
print (numeros)

i = numeros[0]

numeros[0] = numeros [1]
numeros[1] = i

print (numeros)

#-----------------
numeros = [10,20]

if 10 in numeros :
  print ("a lista contém o valor 10")

#Contém/ NÃO CONTÉM

numeros = [10,20]

x= int(input("Digite um número: "))


if x in numeros :
  print (f"a lista contém o valor {x}")
else:
  print (f"a lista não contém o valor {x}")