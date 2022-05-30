# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:07:46 2022

@author: izaro
"""

%reset -f

# Establecemos el directorio
import os
os.chdir(r"C:\NAGORE\PHYTON\CURSO PHYTON SPRI\PythonBasico\5-Fechas\Ejercicios")

# Importamos las librerias necesarias
import pandas as pd
import numpy as np

# Leemos y cargamos los datos
df2=pd.read_csv("Piemonte.csv",sep=",",encoding='latin-1')


#2. Obtener un breve resumen estadístico
# Realizamos un pequeño resumen estadistico de los datos para conocerlos mejor
descripcion = df2.describe()
descripcion


# Como no aparecen todas por consola, podemos hacer un pequeño bucle para que las muestre
for i in df2:
    
    print(df2[i].describe())


#3. Comprobar la tipología de los datos.
df2.dtypes

#4. Transformar la variable ‘Date’ a formato fecha.
#la columna date la considera tipo Object
df2['Date'].describe()    

df2['Date'] = pd.to_datetime(df2['Date'],format='%d/%m/%y')

#5. Comprobar que se ha realizado el cambio correctamente.  
df2['Date'].describe() 


#6. Descomponer la fecha en años.
df2['Año'] =''

for i in range(0,len(df2)):
    df2['Año'][i] = df2['Date'][i].year
    

#7. Crear un nuevo data frame solo con las observaciones del año 2005.