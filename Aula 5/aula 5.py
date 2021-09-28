#Contar caracteres
texto = "texto de teste"

x=len(texto)

print (x)

#Converter um texto para minúsculo

texto = "texto de teste"


print (texto.lower())

#Converter um texto para maiúsculo

texto = "texto de teste"


print (texto.upper())

#Converter a primeira letra da str em MAISUCULO

texto = "texto de teste"


print (texto.capitalize())

#Converter todas as primeiras letras da str em MAIUSCULO

texto = "texto de teste"


print (texto.title())

#Partes da str

txt = "texto de teste"

print (txt[0:5])

#Verificar o inicio ou final de uma str
txt = "texto de teste"

if txt.startswith("texto"):
  print ("inicia com texto")
else :
  print ("nao começa com texto")

------------------------

txt = "texto de teste"

if txt.endswith("teste"):
  print ("inicia com texto")
else :
  print ("nao começa com texto")

#Eliminar espaços na str

txt = " texto de teste "

txt = txt.strip()

print (txt)

#Encontrar um texto na str

txt = "texto de teste"

indice = txt.find("de", 0)

print (indice)

----------------------------

txt = "texto de teste"

indice = txt.find("de")
txt = txt[indice:]

print (txt)

#Substituir o texto na str

txt = "texto de teste"

txt = txt.replace ("texto", "outro")

print (txt)

#Splitar o texto
txt = "daniel;danielbwincardt@gmail.com;dancardt"

palavras = txt.split(";")

nome = palavras [0]
email = palavras [1]
username = palavras[2]

print (f"O nome é: {nome}")
print(f"O email é: {email}")
print (f"O username é: {username}")









