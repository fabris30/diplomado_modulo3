# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:48:35 2022

@author: Fabris
"""
## Miguel Fabris Avila
## cc: 1063719267
## miguel.fabris@upb.edu.co
## ID: 502243
import pandas as pd

persona_1=['Camilo',19,'M',64,1.92,2000,0.2,3,'+573333',6]
persona_2=['Pedro',23,'M',60,1.20,12000,0.7,8,'+57555',18]
persona_3=['Natalia',30,'F',50,1.52,5000,0.5,2,'+576666',12]
persona_4=['Susana',19,'F',56,1.61,2500,0.6,5,'+5733343',24]
persona_5=['Pedro',23,'M',58,1.55,1800,0.12,7,'+5725510',18]
persona_6=['Natalia',25,'F',62,1.73,5300,0.21,5,'+579665',24]
persona_7=['Alvaro',22,'M',70,1.81,3000,0.33,2,'+5788433',6]
persona_8=['Sofia',18,'F',60,1.68,2200,0.65,5,'+5777322',18]
persona_9=['Angela',19,'F',50,1.52,6000,0.51,3,'+57212127',12]
persona_10=['Gustavo',21,'M',79,1.70,2800,0.34,2,'+5790823',24]

lista_info=[persona_1,persona_2,persona_3,persona_4,persona_5,persona_6,persona_7,persona_8,persona_9,persona_10]

datacompa=pd.DataFrame(lista_info,
                  columns=['nombre','edad','genero','peso','estatura','dinero_a_invertir','interes_a_nual','anos_de_inversion','telefono','hora_compra'])

print(datacompa.info())
#Ejercicio 1
# creamos una nueva columna con el imc de cada uno de los compañeros 

imc=datacompa['peso']/(datacompa['estatura'])**2
print('IMC de los compañeros')
print(round(imc,2))
datacompa['imc']=round(imc,2)

# Ejercicio 2
capital= datacompa['dinero_a_invertir']*((datacompa['interes_a_nual']/(100+1))**datacompa['anos_de_inversion'])
datacompa['capital']=capital


# Ejercicio3
precio_pan = 15000

datacompa['descuento']=[(precio_pan*0.1) if s ==6 else (precio_pan*0.2) if s ==12 else (precio_pan*0.3) if s ==18 else (precio_pan*0.4) if s ==24 else (precio_pan*0) for s in datacompa['hora_compra']] 

## pago total
datacompa['pago_total']=precio_pan-datacompa['descuento']

#Ejercicio4
datacompa['extension'] = ["-10" if (g=='F') else ("-11") for g in datacompa['genero']] 

datacompa['telefono']=datacompa['telefono']+datacompa['extension']