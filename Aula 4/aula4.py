#Definindo Funções

def ola() :
  print ('==========')
  print ("alalala")
  print ("kakakakakak")


ola()
ola()
ola()

#Função com 1 parametro

def printNumero(num) :
  print (f"O número é: {num}")

x=10
y=20


printNumero (x)
printNumero (y)

#Função com 2 parametros e retorno

def media(num1, num2) :
  soma = num1+num2
  return soma/2

media1= media(10,20)
media2= media (20,40)

print (media1)
print (media2)

#Função de média com array

def media (numeros): 
  total = 0
  for num in numeros:
    total = total + num
    m = total / len (numeros)
    return m

nums = [10,20,30]

m1 = media(nums)
print(m1)

#Loop Infinito (ou definido até __)

i = 0

while i <10 :
  print (i)
  i = i + 1

#Gerar números aleatórios

import random 

num = random.randrange(1, 10)

print(num)
