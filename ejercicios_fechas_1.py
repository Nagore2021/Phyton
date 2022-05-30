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
df2_2005  = df2[df2['Año']==2005]

#8. Descomponer la fecha en meses.
df2_2005['Mes'] = ''

for i in range(0, len(df2_200df2_5)):
    
#8. ¿Cuántas observaciones se han hecho en cada mes?

df2_2005['Mes'].value_counts()
    df2_2005['Mes'][i] = df2_2005['Date'][i].month
    
#10. Cambiar el formato de la fecha a:
    #a. Nombre completo del día de la semana, Nombre completo del mes, Año
    #en formato largo y Numero del día del año.

# Definimos el formato
formato1='%A %B %Y %j'

df2_2005['Date1']=''
df2['fecha1']=''

from datetime import datetime, date, time, timedelta

for i in range(0,len(df2_2005)):
    df2_2005['Date1'][i] = df2_2005['Date'][i].strftime(formato1)
    
    
for i in range (0,len(df2)):
   df2['fecha1'][i]= df2['Date'][i].strftime(formato1)

#b Nº semana del año, día del mes, año, hora local y nombre de la zona horaria.

formato2='%U %d %y %X %Z'

df2_2005['Date2']=''
df2['fecha2']=''

for i in range(0,len(df2_2005)):
    df2_2005['Date2'][i] = df2_2005['Date'][i].strftime(formato2)

for i in range (0,len(df2)):
   df2['fecha2'][i]= df2['Date'][i].strftime(formato2)


#11. Calcular los días que faltan para que se termine el curso.
hoy = date.today()
hoy
fin_curso= date(2022,6,1)
Dias_terminar_curso= fin_curso - hoy
Dias_terminar_curso

#12. Gráficos:
    #a. Distribución de las precipitaciones
    
    plot = df2['PREC'].plot(figsize=(8, 7))
    
   
    df2['PREC'].plot(kind='box')

    import seaborn as sns
    sns.boxplot(x=df2['Año'], y=df2['PREC'])
    
    
    # Histograma Precipitaciones
    df2.hist(column='PREC')
    
    
    #b. Distribución de ‘ws’ y ‘precipitaciones
    
    plot = df2[['WS','PREC']].plot(figsize=(10, 7))
    
    
    sns.boxplot(x=df2['PREC'], y=df2['WS'])
    
    import matplotlib.pyplot as plt
    plt.plot(df2['PREC'],df2['WS'],'.')
    
    
    
    import numpy as np

    # Hay que ejecutarlo todo a la vez.
    f, ax = plt.subplots(figsize=(10, 8))
    corr = df2.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax)
    
  
    plt.matshow(df2.corr())
    
    datoscomp=df2.dropna()
    sns.pairplot(datoscomp)