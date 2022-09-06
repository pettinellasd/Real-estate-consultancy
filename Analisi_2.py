import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from datetime import datetime
import mysql.connector
import os

start2 = timer()                                               # inizio del timer per il workflow
datetime2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')       # inizio del timestamp

df = pd.read_csv("df.csv", index_col='id')

brooklyn = df.loc[(df['neighbourhood_group'] == 'Brooklyn') & (df['room_type'] == 'Entire home/apt')]   # condizioni da approfondire

br_location = 110 * (np.arccos(np.sin(brooklyn['latitude']) * np.sin(40.706001)         # formula trigonometrica per conversione in km
                               + np.cos(brooklyn['latitude']) * np.cos(40.706001)
                               * np.cos(-73.997002 - brooklyn['longitude'])))
br = brooklyn.copy()        # copia superficiale = qualsiasi modifica nel nuovo elenco non verrà riflessa nell'elenco originale
br['br_location'] = br_location.round(decimals=1)       # per ottenere un solo numero decimale

br_choice1 = br[(br['br_location'] <= 2) & (br['price'] >= 150) & (br['price'] <= 155)]     # condizioni di posizione e di intervalli di prezzo
br_choice2 = br[(br['br_location'] <= 2) & (br['price'] > 155) & (br['price'] <= 160)]
br_choice3 = br[(br['br_location'] <= 2) & (br['price'] > 160) & (br['price'] <= 165)]
br_choice4 = br[(br['br_location'] <= 2) & (br['price'] > 165) & (br['price'] <= 170)]
br_choice5 = br[(br['br_location'] <= 2) & (br['price'] > 170) & (br['price'] <= 175)]

br1 = br_choice1.shape[0]           # per ottenere il numero di righe in uso
br2 = br_choice2.shape[0]
br3 = br_choice3.shape[0]
br4 = br_choice4.shape[0]
br5 = br_choice5.shape[0]

print(br1, br2, br3, br4, br5)

# creazione pie chart con percentuali

labels = '150-155', '155-160', '160-165', '165-170', '170-175'
sizes = [br1, br2, br3, br4, br5]
explode = (0, 0.1, 0, 0, 0)         # effetto grafico per distaccare la fetta interessata

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',   # effetti grafici e creazione percentuale
        shadow=True, startangle=90)
ax1.axis('equal')  # assicura che la torta abbia un disegno circolare (di default è di forma ovalizzata)

ax1.set_title("Campionatura per intervalli di prezzo (%)")
plt2 = plt.savefig('plt2.pdf')
plt.show()

# INIZIO RICERCA PER MANHATTAN A 2 KM DA WALL STREET

manhattan = df.loc[(df['neighbourhood_group'] == 'Manhattan') & (df['room_type'] == 'Entire home/apt')]

mn_location = 110 * (np.arccos(np.sin(manhattan['latitude']) * np.sin(40.7038)
                               + np.cos(manhattan['latitude']) * np.cos(40.7038)
                               * np.cos(-74.0057 - manhattan['longitude'])))
mn = manhattan.copy()
mn['mn_location'] = mn_location.round(decimals=1)

range1 = mn[(mn['mn_location'] <= 2) & (mn['price'] >= 150) & (mn['price'] <= 155)]
range2 = mn[(mn['mn_location'] <= 2) & (mn['price'] > 155) & (mn['price'] <= 160)]
range3 = mn[(mn['mn_location'] <= 2) & (mn['price'] > 160) & (mn['price'] <= 165)]
range4 = mn[(mn['mn_location'] <= 2) & (mn['price'] > 165) & (mn['price'] <= 170)]
range5 = mn[(mn['mn_location'] <= 2) & (mn['price'] > 170) & (mn['price'] <= 175)]

mn1 = range1.shape[0] # Per ottenere il numero di righe in un uso dataframe
mn2 = range2.shape[0]
mn3 = range3.shape[0]
mn4 = range4.shape[0]
mn5 = range5.shape[0]

print(mn1, mn2, mn3, mn4, mn5)

# CREO UN DIAGRAMMA A TORTA CON LE PERCENTUALI
labels = '150-155', '155-160', '160-165', '165-170', '170-175'
sizes = [mn1, mn2, mn3, mn4, mn5]
explode = (0, 0.1, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # assicuro alla torta un aspetto circolare anziché ovale(default)

ax1.set_title("Campionatura per intervalli di prezzo (%)")
plt3 = plt.savefig('plt3.pdf')
plt.show()

filepath2 = os.path.abspath('Analisi_2')
dfpath = os.path.abspath('df')
img2 = os.path.abspath('plt2')
img3 = os.path.abspath('plt3')

end2 = timer()
end2 = (end2 - start2)

mydb = mysql.connector.connect(         # connessione al database creato
    host='localhost',
    user='root',
    password='arcelliboccia',
    database='programming')

mycursor = mydb.cursor()                # il cursore è l'oggetto che mette in comunicazione lo script con MySQL server

# inserisco i valori nei campi
mycursor.executemany("INSERT INTO exam_py (timestamp, analysis, dataframe, images, time) VALUES (%s, %s, %s, %s, %s)",
                     [
                         (datetime2, filepath2, dfpath, img2, end2),
                         (datetime2, filepath2, dfpath, img3, end2)])
mydb.commit()

