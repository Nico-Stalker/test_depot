from pprint import pprint # importe la méthode pprint du module pprint
with open("./access.log", "r") as file_pointer: # Récupérer les lignes du fichier dans une variable
  lines = file_pointer.readlines()  # la variable
# Extraire les données sur des lignes
import re

log_regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.+\] \"[^\"]+\" (\d{3}) \d+"

access_data = []
for line in lines:
  data = re.findall(log_regex, line)[0]
  access_data.append(data)
# Récupérer les adresses IP dans une liste à part
ip_list = [ip for ip, status_code in access_data]
# Compter le nombre d'occurence dans une liste, utiliser Counter du module collections
from collections import Counter
ip_count = {}

for ip in ip_list:
  if ip not in ip_count:
    ip_count[ip] = 1
  else:
    ip_count[ip] += 1
# Compter les code retour/IP
final_data = {}     # Initialiser notre format
# Créer le premier niveau (adresses IP)
for ip, status_code in access_data:
  final_data[ip] = {}
# Créer le dernier niveau (codes retour)
for ip, status_code in access_data:
  if status_code not in final_data[ip]:
    final_data[ip][status_code] = 1
  else:
    final_data[ip][status_code] += 1

pprint(final_data)
# Exporter la donnée en JSON dans un fichier
#import json

#with open("access.json", "w") as json_file_pointer:
  #json.dump(final_data, json_file_pointer)

# Création base de données : https://docs.python.org/3/library/sqlite3.html
# Video The Beginners Guide : https://www.youtube.com/watch?v=5LpotBtmZZs
#import sqlite3
#con = sqlite3.connect("apachelog.db")

#cur = con.cursor()

#cur.execute("CREATE TABLE data(IP, Code retour, Valeur)")

#cur.execute("""
#    INSERT INTO data VALUES
#        (1,2,3)
#""")

#con.commit()
