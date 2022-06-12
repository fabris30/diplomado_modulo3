# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:44:32 2022

@author: Fabris
"""

## Miguel Fabris Avila
## cc: 1063719267
## miguel.fabris@upb.edu.co
## ID: 502243

#se importan las librerias
import pandas as pd
import numpy as np
from sklearn import linear_model


data= pd.read_csv('cars.csv')

df= pd.DataFrame(data)
#A partir de los valores independientes (volumen, peso y producción de CO2) predecir el
#comportamiento de la variable dependiente (marca del carro.)

#se declara una variable lista de marcas
lista_marca = [
    (df["Car"] == "Mitsubishi"),
    (df["Car"] == "Ford"),
    (df["Car"] == "Audi"),
    (df["Car"] == "Honda"),
    (df["Car"] == "Hundai"),
    (df["Car"] == "Opel"),
    (df["Car"] == "BMW"),
    (df["Car"] == "Skoda"),
    (df["Car"] == "Fiat"),
    (df["Car"] == "Hyundai"),
    (df["Car"] == "Suzuki"),
    (df["Car"] == "Volvo"),
    (df["Car"] == "Mazda"),
    (df["Car"] == "Toyoty"),
    (df["Car"] == "Mini"),
    (df["Car"] == "VW"),
    (df["Car"] == "Mercedes"),
   
]

#se crea una lista de numeros rsepcto a la cantidad de marcas en la variable listas_marca
 
cant_lis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

df['marcaCars'] = np.select(lista_marca, cant_lis, default="not_specified")


dataf = pd.DataFrame()

dataf["marca"] = df["Car"].drop_duplicates()

dataf["marcaCars"] = cant_lis

# creamos las variables X, Y 

x = df[['Volume', 'Weight', 'CO2']]

y = df["marcaCars"]

#se convieerten de tipo Arrays las variables X,Y
x = np.array(x)
y = np.array(y)

reg = linear_model.LinearRegression()
reg.fit(x,y)

#con un print se imprime los coeficientes
print(reg.coef_)

#Regresion Multiple 
predicted_Car = reg.predict([[2000, 1746, 117]])

marca_carro=int(np.round(predicted_Car,decimals = 0))

nombre = dataf[dataf["marcaCars"].isin([marca_carro])]
print(df)
print("la marca que de carro que se selecciono fue: ",nombre["marca"].values[0])



