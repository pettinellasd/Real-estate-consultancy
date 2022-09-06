import pandas as pd
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from datetime import datetime
import mysql.connector
import os

start1 = timer()                                               # inizio del timer per il workflow
datetime1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')       # inizio del timestamp

df = pd.read_csv("df.csv", index_col='id')  # apertura del dataframe con impostazione dell'indice in riferimento alla prima colonna

br = df.loc[(df['neighbourhood_group'] == 'Brooklyn') & (df['room_type'] == 'Entire home/apt')]      #selezione delle condizioni all'interno delle colonne
mn = df.loc[(df['neighbourhood_group'] == 'Manhattan') & (df['room_type'] == 'Entire home/apt')]
qs = df.loc[(df['neighbourhood_group'] == 'Queens') & (df['room_type'] == 'Entire home/apt')]
bx = df.loc[(df['neighbourhood_group'] == 'Bronx') & (df['room_type'] == 'Entire home/apt')]
si = df.loc[(df['neighbourhood_group'] == 'Staten Island') & (df['room_type'] == 'Entire home/apt')]

br_meanprice = br.price.mean()          # calcolo del prezzo medio all'interno delle condizione sopra poste
mn_meanprice = mn.price.mean()
qs_meanprice = qs.price.mean()
bx_meanprice = bx.price.mean()
si_meanprice = si.price.mean()

print(br_meanprice, mn_meanprice, qs_meanprice, bx_meanprice, si_meanprice)

# creazione del diagramma

Neigh = ['Brooklyn', 'Manhattan', 'Queens', 'Bronx', 'Staten Island']
pr_mean = [br_meanprice, mn_meanprice, qs_meanprice, bx_meanprice, si_meanprice]
plt.bar(Neigh, pr_mean, color = ('b', 'g', 'r', 'y', 'black'))      # impostazione dell'istogramma
plt.xlabel('Neighbourhood group')
plt.ylabel('Price')
plt1 = plt.savefig('plt1.pdf')
plt.show()

filepath1 = os.path.abspath('Analisi_1')
dfpath = os.path.abspath('df')
img1 = os.path.abspath('plt1')

end1 = timer()
end1 = (end1 - start1)

mydb = mysql.connector.connect(         # connessione al database creato
    host='localhost',
    user='root',
    password='arcelliboccia')

mycursor = mydb.cursor()                # il cursore è l'oggetto che mette in comunicazione lo script con MySQL server

# creo il database
mycursor.execute("CREATE DATABASE programming")

mydb = mysql.connector.connect(         # connessione al database creato
    host='localhost',
    user='root',
    password='arcelliboccia',
    database='programming')

mycursor2 = mydb.cursor()
# creo la tabella impostando i campi
mycursor2.execute("CREATE TABLE exam_py (timestamp DATETIME, analysis VARCHAR(255), dataframe VARCHAR(255), images VARCHAR(255), time FLOAT(40))")

mycursor3 = mydb.cursor()
# inserisco i valori nei campi
sqlFormula = "INSERT INTO exam_py (timestamp, analysis, dataframe, images, time) VALUES (%s, %s, %s, %s, %s)"
insert = (datetime1,
          filepath1,
          dfpath,
          img1,
          end1)
# inserisco nel database
mycursor3.execute(sqlFormula, insert)
mydb.commit()