# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:41:52 2022

@author: Fabris
"""
## Miguel Fabris Avila
## cc: 1063719267
## miguel.fabris@upb.edu.co
## ID: 502243
def ecuacion_1(a,b,c,d,e,f):
    expresio_1 =a+(b/c)
    expresion_2=d+(e/f)
    respuesta=expresio_1/expresion_2
    
    return respuesta
    
    
ecu1=ecuacion_1(11, 4, 4, 3, 2, 2)
print('Resultado de la Ecu1 = ', ecu1)


def ecuacion_2(a,b,c,d):
    expresion= a-(b/(c-d))
    return expresion

ecu2 = ecuacion_2(10, 12, 8, 5)

print('Resultado de la Ecu2= ', ecu2)

if(ecu1==ecu2):
    print('Los valores no se pueden intercambiar por que son iguales, \n y su valor es = ',ecu1)
    
else:
    aux=ecu1
    ecu1=ecu2 
    ecu2=aux
    print('Valores intercambiano son')
    print('Ecu1 = ',ecu1)
    print('Ecu2 = ',ecu2)