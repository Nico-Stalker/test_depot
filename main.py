####################### Parser un fichier de log pour Apache #######################
# Objectif : Créer un script Python permettant de parser des fichiers de log générer par Apache
# et de les restituer dans un fichier JSON ou une base de donnée.

# Enoncé : Le but est d'extraire les connexions d'un fichier de log d'accès et d'indiquer le nombre de chaque code retour pour chaque adresse IP.
# Le resultat devra ensuite être stocké dans un fichier JSON.

# C:\Users\Nico\PycharmProjects\Apache_log_parser\access.log
# C:\Users\Nico\PycharmProjects\Apache_log_parser\example_file.txt

# Lecture du fichier test
#with open("./example_file.txt", "r") as file_pointer:
#  content = file_pointer.read()
#  print(f"Le fichier continent le texte : {content}")

# Lecture du log
#with open("./access.log", "r") as file_pointer:
# content = file_pointer.read()
# print(content)

# Lecture sans saut de ligne
#with open("./access.log", "r") as file_pointer:
# content = file_pointer.read()
# print(content.split("\n"))

# Lecture par readline

with open("./access.log", "r") as file_pointer:
 lines = file_pointer.readlines()

 import re
 regex = r"^(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})"   # r"^(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}) - - \[.+\] \"[^\"]+\" (\d{3}) \d+"
 for line in lines[:]:
     data = re.findall(regex, line)[0]
     #print(data)

import json
with open("file.json", "w") as json_file_pointer:
  json.dump(data, json_file_pointer)

#count = data.count(regex)
#print("Nombre d'adresse IP", count)
