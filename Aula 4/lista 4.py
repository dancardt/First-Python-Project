apostas =[]
nomes =[] 
import random
num = 0




def menu () :
  print ("==========================================")
  print ("Opções: ")
  print ("1 - Adicionar aposta")
  print ("2 - Listar apostas")
  print ("3 - Sortear um número")
  print ("4 - Apresentar o ganhador")
  print ("5 - Sair")

def addAposta():
  aposta = int(input("Digite a sua aposta, entre 1 e 20: "))
  apostas.append (aposta)
  print (aposta)

def addNome():
  nome = (input("Digite o seu nome: "))
  nomes.append (nome)
  print (nome)

def lista():
  for i in range (len(apostas)) :
    aposta = apostas[i]
    nome = nomes [i]
    print (f"Nome: {nome}, Aposta: {aposta}")


def aleatorio():
  sorteio = random.randrange(1, 3)
  print (f"Número sorteado: {sorteio}")
  return sorteio

def ganhador() :
  teveGanhador = 0
  print (num)
  for i in range (len(apostas)) :
    aposta = apostas[i]
    nome = nomes [i]
    if num == aposta :
      print (f"O ganhador é {nome}")
      teveGanhador = 1
  if teveGanhador == 0 :
    print (f"Ninguém ganhou o sorteio!")


opcao = 0

while opcao !=5:
  menu()
  opcao = int(input("Digite a opção: "))

  if opcao == 1:
   addAposta()
   addNome()
  if opcao == 2:
    lista()
  if opcao == 3:
    num = aleatorio()
  if opcao == 4:
    ganhador()


  


print("Acabou o sorteio")