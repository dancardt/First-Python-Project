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
