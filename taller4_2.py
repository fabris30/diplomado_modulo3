# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:15:09 2022

@author: Fabris
"""
## Miguel Fabris Avila
## cc: 1063719267
## miguel.fabris@upb.edu.co
## ID: 502243

########### SEGUNDA PARTE DEL TALLER 4  ###############

#importes de librerias 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# leer el archivos xlsx con pandas
data = pd.read_excel("AirQualityUCI.xlsx")

# Declaramos las variable de X, Y
x = data["NO2(GT)"]

y = data["T"]

la_X = x[:8000]
la_Y = y[:8000]

p_X = x[8000:]
p_Y = y[8000:]

#modelo polinomial​

modelo = np.poly1d(np.polyfit(la_X, la_Y, 3))

# Definimos el espaciamiento para la linea
myline = np.linspace(100, 1000, 8000)

# Graficamos la línea de regresión polinomial

plt.scatter(la_X,la_Y)
plt.plot(la_X, modelo(myline))
plt.show()
r2 = r2_score(la_Y, modelo(la_X))
print("R cuadrado: ")
print(r2)
