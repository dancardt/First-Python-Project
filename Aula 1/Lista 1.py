#Lista de Exercícios 1
#Exercício 1
a = float (input ("Digite a nota da P1: "))
b = float (input ("Digite a nota da P2: "))
c = float (input ("Digite a nota da P3: "))

media = round ((a+b+c)/3, 2)

print ("Sua média é: " + str (media))


if media >=7 :
  print ("Aprovado")
else:
  print ("Não aprovado")

#Exercício 2
a = int (input ("Digite o primeiro número: "))
b = int (input ("Digite o segundo número: "))
c = int (input ("Digite o terceiro número: "))

maior = 0
if a > b and a > c :
  maior = a

if b > c  and b > a :
  maior = b

if c > a and c > b :
  maior = c

print ("O maior número é: " + str (maior))

maior = 0
if a > b :
  if a > c :
    maior = a



#Exercício 3
base = float (input ("Digite o valor da base: "))
altura = float (input ("Digite o valor da altura: "))

área = base*altura
peri = base+base+altura+altura

print ("A área do retângulo é de: " + str (área))
print ("O perímetro corresponde a: "+ str (peri))

#Exercício 4
face = float (input ("Digite o valor de um dos lados do quadrado: "))

área = face*face
peri = 4*face

print ("A área do quadrado é de: " + str (área))
print ("O perímetro corresponde a: "+ str (peri))

#Exercício 5
a = float (input ("Digite um número: "))

sucessor = (a+1)
print ("O sucessor de " + str (a) + " é " + str (sucessor))

#Exercício 6
a = float (input ("Digite um número: "))

if a < 0:
  print ("O valor é negativo")
else :
  print ("O valor é positivo")

#Exercício 7
a = float (input ("Digite um número: "))

par = a%2

if par!=1 :
  print ("Este número é par")
else :
  print ("Este número é ímpar")

#Exercício 8
a1 = float(input("Primeiro número: "))
a2 = float(input("Segundo número: " ))
a3 = float (input("Terceiro número: "))
 
p1 = 5
p2 = 2.5
p3 = 2.5
 
if a1 > a2 and a1 >a3 :
 mediap = (a1 * p1 + a2 * p2 + a3*p3) / p1 + p2 + p3
if a2 > a1 and a2 > a3 :
 mediap = (a1 * p2 + a2 * p1 + a3  *p3) / p1 + p2 + p3
if a3 > a1 and a3> a2:
 mediap = (a1 * p2 + a2 * p2 + a3 * p1) / p1 + p2+ p3
 
print ("A média ponderada é {}".format(mediap))

#Exercício 9
print ("Que dia da semana é hoje?")

a = int (input ("Digite um número: "))

if a==1 :
  print ("O dia da semana é: Domingo")
if a==2 :
  print ("O dia da semana é: Segunda")
if a==3 :
  print ("O dia da semana é: Terça")
if a==4 :
  print ("O dia da semana é: Quarta")
if a==5 :
  print ("O dia da semana é: Quinta")
if a==6 :
  print ("O dia da semana é: Sexta")
if a==7 :
  print ("O dia da semana é: Sábado")

if a > 7 or a < 1 :
  print ("Error - Digíte um número de 1 a 7")








