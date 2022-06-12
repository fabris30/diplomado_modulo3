# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 12:40:17 2022

@author: Fabris
"""

## Miguel Fabris Avila
## cc: 1063719267
## miguel.fabris@upb.edu.co
## ID: 502243

########### SEGUNDA PARTE DEL TALLER 4  ###############

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# leemos el archivos csv con la libreria de pandas
df = pd.read_excel("AirQualityUCI.xlsx")

# creamos las variables   X,Y
x = df["NO2(GT)"]

y = df["T"]

x,y = np.array(x).reshape(-1,1), np.array(y)

la_X = x[:8000]
la_Y = y[:8000]

p_X = x[8000:]
p_Y = y[8000:]


modelo = linear_model.LinearRegression().fit(la_X,la_Y)

#el r cuadrado
r_sq = modelo.score(la_X,la_Y)
r_sq_test = modelo.score(p_X,p_Y)
#predicion de valores 
y_pred = modelo.predict(p_X)
# dispersion 
plt.scatter(p_X,p_Y)
plt.plot(p_X, y_pred)
plt.show()

print("El R es:", r_sq)
print("Predicion", r_sq_test)
print("")