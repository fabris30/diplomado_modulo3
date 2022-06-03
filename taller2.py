# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:31:39 2022

@author: Fabris
"""
## Miguel Fabris Avila
## cc: 1063719267
## miguel.fabris@upb.edu.co
## ID: 502243
import pandas as pd
import numpy as np

data = pd.read_csv('netflix_titles.csv')

# las primeras y ultimas 5 filas del arreglo
df=pd.DataFrame(data.head())
print(df)

ultimasfilas=pd.DataFrame(data.tail())
print(ultimasfilas)

# tipos de datos 
data.info()

datatitulo=pd.DataFrame(data['title'])

# exportarlo en un archivo xlsx
datatitulo.to_excel('Netflix_list.xlsx', index=False)

# Cree una nueva data frame en el cual segmente únicamente: el tipo, la duración, la
# descripción y el país

newdf=pd.DataFrame(data[['type','country','duration','description']])
newdf['duration'].info()
 # separamos las columnas de duracion 
duracion=newdf['duration'].str.split(expand=True)
duracion.columns=['duracion','tipo_duracion']
newdf=pd.concat([newdf,duracion],axis=1)

newdf.drop(columns=['duration'], inplace=True)
newdf['duracion']=newdf['duracion'].astype(float)
print(newdf)


# filtarmos los datos mayores a 100 minutos 

duracion_min = newdf[newdf['tipo_duracion'].isin(['min'])]
mayor_100_min=duracion_min[duracion_min['duracion']>100.0]

# Haga un filtro para los “TV Shows” que tienen más de 3 temporadas.

tv_Shows = newdf[newdf['type'].isin(['TV Show','Seasons'])]
tv_Shows_mas_3_temp=tv_Shows[tv_Shows['duracion']>3]
# Haga un filtro en el cual solo tenga en cuenta 2 categorías/etiquetas (libre elección).

tv_Shows_country = newdf[newdf['type'].isin(['TV Show']) & newdf['country'].isin(['India'])]

# 11. Añada una nueva columna “Visto”, en la cual debe colocar 1/0 (aleatorio) si vio o no el show
# (simulación).

np.random.seed(0)
x=np.random.randint(0,2,size=8807)
print(x)
newdf['vistas']=x


