import numpy as np
import pandas as pd
import datetime
from matplotlib import pyplot as plt


# On crée un tableau ne contenant que : le temps, l’altitude, la pulsation et la vitesse :
columns = ['Time', 'Altitude (m)', 'Heart rate (bpm)', 'Speed (km/h)']
data = pd.read_excel('coureur1.xls',usecols=columns)
print(data)
# Trouver une méthode permettant d’effacer les lignes contenant un "Nan"

new_data = data.dropna()
print(new_data)


# Calculer la vitesse maximale et minimale atteinte par le coureur
vitesse_maximale = new_data['Speed (km/h)'].max()
vitesse_minimale = new_data['Speed (km/h)'].min()


print("La vitesse max est de : ",vitesse_maximale," km/h.\nLa vitesse min est de : ",vitesse_minimale,"km/h.")

# On s'assure que la colonne 'Time' est de type datetime :

new_data['Time'] = pd.to_datetime(new_data['Time'])
# new_data['Time'] = pd.to_datetime(new_data['Time'], format='%H:%M:%S')

new_data.loc[:, 'hours'] = new_data['Time'].dt.hour
new_data.loc[:, 'minute'] = new_data['Time'].dt.minute
new_data.loc[:, 'secondes'] = new_data['Time'].dt.second


# new_data['hours'] = new_data['Time'].hour
# new_data['minute'] = new_data['Time'].minute
# new_data['secondes'] = new_data['Time'].second
print(new_data)



# On trace la vitesse en fonction du temps :
new_data.plot(x='Time', y='Speed (km/h)', kind='line', title='Vitesse en fonction du temps')
plt.savefig('Vitesse en fonction du temps.png', format='png', dpi=200)
plt.show()

# On trace l’altitude en fonction du temps :
new_data.plot(x='Time', y='Altitude (m)', kind='line', title='Altitude en fonction du temps')
plt.savefig('Altitude en fonction du temps.png', format='png', dpi=200)
plt.show()

# On trace la pulsation en fonction du temps :
new_data.plot(x='Time', y='Heart rate (bpm)', kind='line', title='Pulsation en fonction du temps')
plt.savefig('Pulsation en fonction du temps.png', format='png', dpi=200)
plt.show()

# La vitesse moyenne :
vitesse_moyenne = new_data['Speed (km/h)'].mean()
print("La vitesse moyenne est de : ",vitesse_moyenne,"km/h.")

