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

mediasb = []
mediasa = []

for i in range (len(notas)):
  if nota > media:
    mediasa.append(nota)
else:
  mediasb.append(nota)




print(media)
print(f"Existem {mediasa} alunos com a nota acima da média na turma ")

#Exercício 3 - NAO FEITO

#Exercício 4

numeros = []

for i in range (5) :
  numero = input ("Digite um numero: ")
  numeros.append(numero)

print (list(reversed(numeros)))

#Exercício 5

#Exercício 6

#Exercício 7

numeros = []

for i in range (10) :
  numero = int (input ("Digite um numero: "))
  numeros.append(numero)
  numeros.sort()
print (f"A lista ordenada em ordem crescente: {numeros}")