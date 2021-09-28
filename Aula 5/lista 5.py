#Exercício 1

nome = str(input("Digite seu nome completo: "))

indice = nome.find (" ")
primeironome = nome[0:indice]

print (f"O seu nome é: {primeironome}")

#Exercício 2

frases = []


def addFrase():
  for i in range (3) :
    frase = (input(f"Digite aqui a frase {i+1}: "))
    frases.append (frase)
    print (frase)

def busca() :
  txt = (input("Digite aqui sua busca:"))
  for texto in frases :
    if texto.find (txt) != -1:
      print (texto)

addFrase()
busca()

#Exercício 3

x = input ("Digite uma frase: ")

palavras = x.split(" ")
palavras.reverse()

for palavra in palavras :
  print(palavra)

#Exercício 4

import sys

while True :
  x = input("Digite a expressão: ")

  if x == "sair" :
    sys.exit()

  exp = x.split()

  operacao = exp[0]
  num1 = float(exp[1])
  num2 = float (exp[2])

  if operacao == "somar" :
    res = num1 + num2
    print (res)

  if operacao == "dividir" :
    res = num1/num2
    print (res)

  if operacao == "multiplicar" :
    res = num1*num2
    print (res)

  if operacao == "subtrair" :
    res = num1-num2
    print(res)
  

#Exercicio 5

cad = "nome=Robson,email=robson.luz@fae.edu;nome=Joao,email=joao@email.com"

usuarios = cad.split(";")
user = cad.split(",")

nome = user[0]
indice = nome.find("=")



print ("Usuários cadastrados: " + str (len(usuarios)))
print ("===============================")

