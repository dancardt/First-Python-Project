#Exercício 1

nomes = []
 
for i in range (10):
 nome = input("Digite um nome: ")
 nomes.append(nome)
 
print ("------")
 
ultnome = input("Digite um último nome: ")
if ultnome in nomes:
 print ("Achei")
else:
 print ("Não achei")

#Exercício 2 - INCOMPLETO

notas = []


for i in range (5) :
  nota = int(input("Digite sua nota: "))
  notas.append(nota)
  contagem = len(notas)



soma = notas [0] + notas [1] + notas [2] + notas [3] + notas [4] 
media = soma / contagem
print (f"A média da turma é {media}")
print (f"Alunos presentes: {contagem}")

#Exercício 3

numeros = []
maior = 0
menor = 9999999

for i in range (5) :
  numero = int(input("Digite o número: "))
  numeros.append(numero)

for i in range (5):
  if numeros[i] >maior:
    maior=numeros[i]
  if numeros [i] < menor:
    menor = numeros [i]

print (f"Os valores da lista são: {numeros}")
print (f"O maior número é: {maior}")
print (f"O menor número é: {menor}") 


#Exercício 4

numeros = []

for i in range (5) :
  numero = input ("Digite um numero: ")
  numeros.append(numero)

print (list(reversed(numeros)))

#Exercício 5

lista1 = [2,4,6,8,10]
lista2 = [3,4,7,8,10]

print (f"Os valores na lista 1 são: {lista1}")
print (f"Os valores na lista 2 são: {lista2}")

count = 0
for i in range (len(lista1)) :
  if lista1[i] == lista2[i] :
    count = count + 1

print (f"Existem {count} números iguais na mesma posição. ")

#Exercício 6


#Exercício 7

numeros = []

for i in range (10) :
  numero = int (input ("Digite um numero: "))
  numeros.append(numero)
  numeros.sort()
print (f"A lista ordenada em ordem crescente: {numeros}")