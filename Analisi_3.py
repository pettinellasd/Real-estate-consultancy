import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from datetime import datetime
import folium
import mysql.connector
import os

start3 = timer()                                               # inizio del timer per il workflow
datetime3 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')       # inizio del timestamp

df = pd.read_csv("df.csv", index_col='id')
df = df.dropna()

manhattan = df.loc[(df['neighbourhood_group'] == 'Manhattan') & (df['room_type'] == 'Entire home/apt')]

mn_location = 110 * (np.arccos(np.sin(manhattan['latitude']) * np.sin(40.7038)
                               + np.cos(manhattan['latitude']) * np.cos(40.7038)
                               * np.cos(-74.0057 - manhattan['longitude'])))
mn = manhattan.copy()
mn['mn_location'] = mn_location.round(decimals=1)

range2 = mn[(mn['mn_location'] <= 2) & (mn['price'] > 155) & (mn['price'] <= 160)]

#rappresento la fetta di torta che vado ad analizzare ulteriormente, la ordino e prendo i primi 10 risultati
pie = range2[['number_of_reviews', 'last_review', 'latitude', 'longitude', 'host_name']].sort_values(by=['number_of_reviews'], ascending=False).head(10)
print(pie)

# creazione di un istogramma
pie.plot.bar(x='last_review', y='number_of_reviews', rot=25, color='m') # rotazione delle date
plt4 = plt.savefig('plt4.pdf')
plt.show()

# creazione di una mappa
locations = pie[['latitude', 'longitude']]
lat_list = pie['latitude'].values.tolist()
lon_list = pie['longitude'].values.tolist()
locationlist = locations.values.tolist() # creo una lista di liste con lat-lon
len(locationlist) # lunghezza lista per fare il ciclo
host_name = pie['host_name'].values.tolist() # lista con host name
# carico un punto medio per centrare la mappa. Zoom in base al DF
ave_lat = pie['latitude'].mean()
ave_lon = pie['longitude'].mean()
m = folium.Map(location=[ave_lat, ave_lon], zoom_start=11.5)
for point in range(0,len(locationlist)):
    folium.Marker(locationlist[point],popup=host_name[point]).add_to(m)
m.save('map.html')

end3 = timer()
end3 = (end3 - start3)

filepath3 = os.path.abspath('Analisi_3')
dfpath = os.path.abspath('df')
img4 = os.path.abspath('plt4')
map = os.path.abspath('map')

mydb = mysql.connector.connect(         # connessione al database creato
    host='localhost',
    user='root',
    password='arcelliboccia',
    database='programming')

mycursor = mydb.cursor()
# inserisco i valori nei campi
mycursor.executemany("INSERT INTO exam_py (timestamp, analysis, dataframe, images, time) VALUES (%s, %s, %s, %s, %s)",
                     [
                         (datetime3, filepath3, dfpath, img4, end3),
                         (datetime3, filepath3, dfpath, map, end3)])
mydb.commit()