#Iteração
for i in range (10) :
  print (i)

for i in range (10,20) :
  print (i)

#Iteração 
for i in range (1,10,2) :
  print (i)

#Iteração inversa
for i in range (10,0,-1) :
  print (i)

#Iteração com input
for i in range (4) :
 num = int (input("Digite o número " + str (i) + ": "))  
 print ("Você digitou: " + str (num))

#Iteração com range dinâmico
n = int(input ("Digite n: "))
soma = 0

for i in range (n) :
 num = int (input("Digite o número " + str (i) + ": "))  
 soma = soma + num

print (soma)

#Precificação com prestações
valor = int(input ("Digite o valor da compra: "))


for i in range (1,25) :
  prest = valor/i
  prest = round (prest, 2)
  print (str (i) + "x de R$ " + str (prest))