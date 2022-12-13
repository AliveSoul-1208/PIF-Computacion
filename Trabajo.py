import streamlit as st
st.write(""" # Mi Primera aplicacion
Primera *Parte*""")

st.write("""
# Sales model 
Bellow are our sales predictions
for this customer.
""")


#Importamos librerias para Ciencia de Datos y Machine Learning
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt


# In[2]:


#archivo CSV separado por comas
archiv = pd.read_csv('Pelicula.csv',
engine='python')

#leer  lineas
archiv


# In[3]:


archiv.shape


# In[4]:


archiv.dtypes


# In[5]:


archiv.isnull().sum()


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## 2.- Correlación de Pearson  (Similitud) y Sustitución de los NAN

# In[6]:


n = archiv[archiv.columns[1:]].to_numpy()
m = archiv[archiv.columns[0]].to_numpy()
print(n)
print(m)


# In[7]:


n.T


# In[8]:


# Haciendo la Traspuesta para ordenar la tabla
tnsp = pd.DataFrame(n.T, columns = m)
tnsp


# In[9]:


tnsp.describe()


# In[10]:


Elim=tnsp.dropna(axis = 1, how = "all")
Elim


# In[11]:


# Reeemplazando Valores perdidos con el promedio
data_f = Elim.fillna(Elim.median(numeric_only=True))
data_f


# In[12]:


data_f.info()


# In[13]:


data_f


# ## Correlación en pandas

# In[14]:


panda_corr = data_f.corr().round(3)
panda_corr


# In[15]:


panda_corr.describe()


# In[16]:


panda_corr.isnull().sum()


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## 4.- Matrix de Correlación nuestra

# In[17]:


import statistics
import math
lista_u=['klajo', 'ccamilaqu', 'agomeztit', 'rabrilm', 'acamargoca', 'Kvaleroa',
       'elhuamani', 'mlh.melody.2002', 'eduvargasrivera223', 'shanccohui',
       'efloresmal', 'mcaceresramo', 'sebascorr3', 'yessicasuarez0820',
       'psanchezsa', 'suareznieblerafael2021', 'imontalvo', 'rparedesmor',
       'teleco.god', 'brisarakionera', 'raulcornejoapaza', 'jmendozaco',
       'paricahuabrayan', 'bchavezcha', 'mccahuanaq', 'mlh.melody.2001',
       'lugim.2002', 'alivesoul.2002', 'Chesterymaria2017', 'rxanderpq',
       'ifigueroas', 'vichciro', 'correodeciro1234', 'asalinasal', 'amifisa69',
       'eyucrasul', 'oscarelicv', 'fmirandaa', 'cmaron', 'mmendozala']
colist=[]


for j in lista_u:
    for i in lista_u:
        x=data_f[i]    
        y=data_f[j]
        prod=x*y
        x2=x**2
        y2=y**2
    
        px=x.mean()
        py=y.mean()
        pxy=prod.mean()
        cv=pxy-(px*py)

        px2=x2.mean()
        py2=y2.mean()

        dx=math.sqrt(px2-(px**2))
        dy=math.sqrt(py2-(py**2))

        cofp=cv/(dx*dy)

        colist.append(cofp)
        
colist
 
Listf = [round(x,3) for x in colist]


# In[18]:


matf=np.array(Listf).reshape(40,40)
matf


# In[29]:


#CONVIRTIENDO EN TABLA DE CORRELACION
import pandas as pd

print("NumPy Data Array is:")
print(matf)

print("")

Nuestro_corr = pd.DataFrame(matf, index=lista_u, columns=lista_u)
Nuestro_corr


# ## Gráfica de Calor

# <div class="alert alert-info">
# 
#     
#    **HALLAR**: a partir de la matriz de correlación en  <strong>Pandas</strong> .
#     
#    **Instalar** : `matplotlib` `seaborn`
#     
# </div>

# In[20]:


#Mapa de calor de la correlacion de Pandas
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
f = plt.figure(figsize=(12,9))
plt.matshow(data_f.corr(), fignum=f.number)
plt.xticks(range(data_f.shape[1]), data_f.columns, fontsize=8, rotation=90)
plt.yticks(range(data_f.shape[1]), data_f.columns, fontsize=8)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlacion Pandas', fontsize=16)
plt.show()


# In[30]:


import matplotlib.pyplot as plt
f = plt.figure(figsize=(12,9))
plt.matshow(Nuestro_corr, fignum=f.number)
plt.xticks(range(Nuestro_corr.shape[1]), Nuestro_corr.columns, fontsize=8, rotation=90)
plt.yticks(range(Nuestro_corr.shape[1]), Nuestro_corr.columns, fontsize=8)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Matriz de Correlación Nuestra ', fontsize=16)
plt.show()


# ## 5.- RESULTADOS 

# Los resultados de similitud obtenidos en la **Encuesta de PELICULAS** según la tabla de **Correlación** con los siguientes encuestados:
# 
#  1. _paricahuabrayan@gmail.com_ y _teleco.god@gmail.com_  obtienen el **PRIMER** indice mas alto de similitud con 0.871
#  
#  2. _teleco.god@gmail.com_ y _brisarakioneira@gmail.com_ obtienen el **SEGUNDO** indice mas alto de similitud con 0.773

# <div class="alert alert-info">
# 
#     
#    **HALLAR**: a partir de la matriz de correlación en  <strong>Pandas</strong>. A simple vista se puede observar los resultados, pero para una matriz mas grande se debe programar una `función` o `método` para que **localice los dos usuarios con mas alto valos de correlación**.
#     
# </div>

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <center> <h1>Validación de Resultados</h1> </center> 

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## Validación - Matrix de Correlación

# 
# <div class="alert alert-info">
# 
#    Se debe llenar la tabla de __VALIDACIÓN de la Matriz de Correlación__ con los valores de `Similitud` obtenidos
#     
#     
#    En `NUMPY` a partir de las matrices `n` y `m` con funciones.
#     
# </div>

# ### Validacion de resultados del panda

# In[22]:


#VALORES ALTOS DE SIMILITUD EN PANDAS
def busqueda():
    Busqueda1 = panda_corr[panda_corr!=1].max()
    valor1 =np.max(Busqueda1)
    print( 'El 1er mayor valor de similitud es:',valor1)
    Busqueda2 = panda_corr[panda_corr<(valor1)].max()
    valor2 =np.max(Busqueda2)
    print( 'El 2do valor mayor despues del primero es:',valor2)
busqueda()
A = np.array(panda_corr)
x = np.where(np.all(A==0.871,axis=0))
A[:,x]


# In[23]:


#EL CORREO Y PUNTAJE CORRESPONDIENTE SON:
maxim = panda_corr.unstack()
print(maxim.sort_values(ascending=False)[range(len(panda_corr),((len(panda_corr)+4)))])


# ### Validacion de resultados nuestra

# In[31]:


#VALORES ALTOS DE SIMILITUD EN NUESTRA MATRIZ DE CORRELACION
def busqueda():
    Busqueda1 = Nuestro_corr[Nuestro_corr!=1].max()
    valor1 =np.max(Busqueda1)
    print( 'El 1er mayor valor de similitud es:',valor1)
    Busqueda2 = Nuestro_corr[Nuestro_corr<(valor1)].max()
    valor2 =np.max(Busqueda2)
    print( 'El 2do valor mayor despues del primero es:',valor2)
busqueda()
A = np.array(matf)
x = np.where(np.all(A==0.871,axis=0))
A[:,x]


# In[32]:


#EL CORREO Y PUNTAJE CORRESPONDIENTE SON:
maxim = Nuestro_corr.unstack()
print(maxim.sort_values(ascending=False)[range(len(Nuestro_corr),((len(Nuestro_corr)+4)))])


# In[25]:


print( 'Los primeros correos con mayor valor de similitud y puntaje son: \n \n paricahuabrayan y teleco.god con 0.871 \n')

print( 'Los segundos correos con mayor valor de similitud mayor despues del primero son: \n \n brisarakionera y teleco.god con 0.773')


# Se realiza la validación de los resultados obtenidos con la   `Matriz de Correlación de Pearson` en `Numpy` 
#  

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <center> <h1>Conclusiones</h1> </center> 

#  <div class="alert alert-info">
#     
#    - ¿Se valido o no los resultados?
#    - Los resultados Validados son:
#    - ¿Es efectivo el metodo de correlación de pearson?
#    - Correlación de Pearson y Regresión Lineal, ¿cual es su relación?
#     
#  </div>

# ### <font color='blue'> ¿Son valido o no los resultados?</font>
# Los datos fueron sacados de una encuesta confiable,relizada por mi grupo los resultados expresados son corroborados por una serie de codigos importados de la biblioteca pandas y numpy los cuales arrojaron las posibles relaciones exitentes entre los datos ya sea su grado de similitud sus maximos y minimos ,la correlacion que exiten entre estos .etc

# ### <font color='blue'>¿Es efectivo el metodo de correlación de pearson?</font>
# La correlacion de pearson su sa l para calcular la la correlacion de dos datos en general se trata de 'x' y ',Para una busqueda de muchos datos esta no seria efectivo ,ya ue esta destinado al uso de 2 datos,ademas que las variables que se nesesita deben ser medidads a un nivel cuantitativo continuo. Ademas la distribucion de las variables deben ser semejantes a la curva normal. A menos que buaquemos la compracion entre dos datos para ver si coinciden en difernetes aspectos

# ### <font color='blue'>Los resultados Validados son:</font>
# De acuerdo a la correlación de pandas, al igual en la misma matriz de correlacion creada por un algoritmo de nosotros los resultados obtenidos fueron los mismos, los resultados validados y con mayor similitud son:
# 
# **Los primeros correos con mayor valor de similitud y puntaje son:** 
#  
#  paricahuabrayan y teleco.god con 0.871 
# 
# **Los segundos correos con mayor valor de similitud mayor despues del primero son:** 
#  
#  brisarakionera y teleco.god con 0.773
#  
# con esto confirmamos que los resultados son los mismos

# ###  <font color='blue'>Correlación de Pearson y Regresión Lineal, ¿cual es su relación?</font>
# La correlacion lineal es un metodo estadistico que permite cuantificar la relacion lineal entre dos variables . El coeficiente dde correlacion de Pearson es una pruba que mide la relacion estidistica entre dos variables continuas ,lo cual esta ligado con la regresion lineal ya que cuentan con un rango que se establece de +1 y -1 ademas al igual que una regresion lineal mientras el valor de una varible aumenta la otra disminuye .
# Para llevar a cabo la correlacion Pearson.

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## Referencia

# - __Profesor de Matematicas__: `John Gabriel Muñoz Cruz`
# https://www.linkedin.com/in/jgmc
# 
# - __Tutorial de matriz de correlacion__: https://www.instintoprogramador.com.mx/2020/11/tutorial-de-matriz-de-correlacion-de.html
# - __correlacion lineal__:https://www.cienciadedatos.net/documentos/pystats05-correlacion-lineal-python.html
# - __correlacion y regresiopn lineal__:https://www.cienciadedatos.net/documentos/24_correlacion_y_regresion_lineal
# - __Convertir Listas a un Array__: https://blog.finxter.com/como-convertir-una-lista-en-un-array-de-numpy/#:~:text=La%20forma%20m%C3%A1s%20simple%20de,devuelve%20un%20array%20de%20NumPy.&text=Esto%20crea%20una%20nueva%20estructura%20de%20datos%20en%20memoria
# - __numpy a columnas__:https://www.delftstack.com/es/howto/numpy/numpy-add-column/
# - __Libro de datos__:https://libroweb.alfaomega.com.mx/book/962/free/data/Cap14.pdf
# - __Coeficiente de correlacion__:https://www.superprof.es/apuntes/escolar/matematicas/estadistica/disbidimension/coeficiente-de-correlacion.html
# - __Mapa de calor__:https://statologos.com/heatmap-python/
# - __Añadir filas y columnas__:https://es.stackoverflow.com/questions/250622/a%C3%B1adir-nuevas-filas-%C3%B3-columnas-a-matriz-numpy

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)
