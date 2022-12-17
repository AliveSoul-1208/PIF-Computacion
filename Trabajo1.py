import streamlit as st

st.write(""" """)


st.markdown("<h1 style='text-align: center; color: white;'>Universidad Nacional de San Agustín de Arequipa</h1>", unsafe_allow_html=True)

# 
st.markdown("<h1 style='text-align: center; color: white;'>Escuela Profesional de Ingeniería de Telecomunicaciones</h1>", unsafe_allow_html=True)
st.write("""# ![image.png](https://www.unsa.edu.pe/ouresponsabilidadsocial/wp-content/themes/observatorio/img/unsa-logo.png) """)
# 

st.write("""## Ingeniero Renzo Bolivar - Docente DAIE""")

st.write("""# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)""")

st.write("""## GRUPO B - Nº2""")
st.write("""## Alumnos:""")  

st.write("""
###     Miguel Angel Ccahuana Quispe
###     Brayan Enrique Paricahua Choque
###     Jose Luis Mendoza Condo
###     Piero Joseph Sanchez Sanchez""") 

st.write("""# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)""")
st.write("""# INVESTIGACIÓN FORMATIVA""")
 
st.write("""# PROYECTO FINAL""")
st.write("""## PYTHON - Inteligencia Artificial""")

st.write("""# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)""")

st.write("""## OBJETIVOS""")

st.write("""### Los Objetivos de la investigación formativa son:""")
st.write("""
 - **Competencia Comunicativa** Presentación de sus resultados con lenguaje de programación Python utilizando los archivos Jupyter Notebook.
 - **Competencia Aprendizaje**: con las aptitudes en **Descomposición** (desarticular el problema en pequeñas series de soluciones), **Reconocimiento de Patrones** (encontrar simulitud al momento de resolver problemas), **Abstracción** (omitir información relevante), **Algoritmos** (pasos para resolución de un problema).
 - **Competencia de Trabajo en Equipo**: exige habilidades individuales y grupales orientadas a la cooperación, planificación, coordinación, asignación de tareas, cumplimiento de tareas y solución de conflictos en pro de un trabajo colectivo, utilizando los archivos Jupyter Notebook los cuales se sincronizan en el servidor Gitlab con comandos Git.""")

st.write("""# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)""")

st.write("""# Aplicación en IA""")
st.write("""## Sistema Recomendador """)

st.write("""# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png) """)

st.write(""" El Sistema recomendador deberá encontrar la compatibilidad o similitud entre un grupo de personas encuestadas, en el área de: """)

#    
st.write("""    *Peliculas*""")
#     
# 
#     
# 
# 

# 
#     
st.write(""" La compatibilidad o similitud será encontrada con el algoritmo de Correlación de Pearson y será verificada con la La Matrix de Correlación de Pearson con una librería de Python y utilizando una función personal""")
#     


st.write("""# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png) """)

st.write("""### Base Teórica """)


st.write("""### Análisis de Correlación """)

st.write("""##### El *análisis de correlación* es el primer paso para construir modelos explicativos y predictivos más complejos. """)

st.write("""### Correlacion de pearson""")

st.write(""" ##### El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.
 Es el método de correlación más utilizado, pero asume que:
La tendencia debe ser de tipo lineal.No existen valores atípicos (outliers).Las variables deben ser numéricas.Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones
Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.""")

st.write(""" ### Como se interpreta?""")

st.write(""" ##### El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.
un valor positivo indica una relación directa o positiva,un valor negativo indica relación indirecta, inversa o negativa,un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).
 La magnitud nos indica la fuerza de la relación, y toma valores entre −1 a 1. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o −1) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.
si la correlación vale 1 o −1 diremos que la correlación es “perfecta”,si la correlación vale 0 diremos que las variables no están correlacionadas.""")

st.write("""# ![linea 2](https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png) """)

st.write("""### Regresion lineal""")

st.write("""# ![linea 2](https://user-images.githubusercontent.com/25250496/204172072-0fabbfdf-1c4c-4f9b-8f42-505d98b18b71.png) """)

st.write("""### Tamaño de efecto""")

st.write("""En estadística, el tamaño del efecto es una medida de la fuerza o magnitud de un fenómeno. El coeficiente de correlación es una medida del tamaño del efecto para la relación (lineal) entre dos variables numéricas.Se trata de un dato esencial para interpretar los resultados de nuestro estudio y su ausencia en los artículos científicos se ha identificado como uno de los 7 fallos más comunes en investigación (según la APA 19961 , 20012 ).Para interpretar qué tan fuerte es la correlación podemos utilizar el criterio de Cohen (1988)3, quien para valores absolutos indica que valores entre:- .1-.3 representan un efecto pequeño,- .2-.5 un efecto medio- .3.5 un efecto grande.Son valores arbitrarios que te pueden servir de guía, pero te recomiendo interpretar la fuerza (o tamaño) de la correlación según el contexto de tu investigación. No es lo mismo analizar datos de un experimento físico controlado donde habrá poco ruido en los datos, que analizar datos sociales o biológicos donde se espera encontrar menores valores de correlación debido a la gran cantidad de dispersión o variabilidad de los datos.""")

st.write("""Como se mided la correlacion""")

st.write("""Veamos ahora los coeficientes de correlación más utilizados.Tenemos el coeficiente de correlación lineal de Pearson que se sirve para cuantificar tendencias lineales, y el coeficiente de correlación de Spearman que se utiliza para tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas (las variables tienden a moverse en la misma dirección relativa, pero no necesariamente a un ritmo constante; Figura 2).""")

st.write(' A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación. Se trata de una de las técnicas más habituales en análisis de datos y el primer paso necesario antes de construir cualquier <modelo explicativo o predictivo más complejo Para poder tener el  Datset hay que recolectar información a travez de encuentas. A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación. Se trata de una de las *técnicas más habituales en análisis de datos* y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo. Para poder tener el  Datset hay que recolectar información a travez de encuestas.')
st.write("""# ![linea 2](https://www.maximaformacion.es/wp-content/uploads/2021/07/Que-es-la-correlacion-Relacion-lineal-y-relacion-no-lineal.png.webp) """)

st.write("""El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas:""")

st.write("""Es el método de correlación más utilizado, pero asume que:
La tendencia debe ser de tipo lineal.No existen valores atípicos (outliers).Las variables deben ser numé Si las variables son de tipo ordinal (como las preguntas en escala de likert), no podremos aplicar la correlación de Pearson.Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).
Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.""")

st.write("""### Mapas de calor""")

st.write("""En una entrada anterior se han visto algunos de los gráficos más importantes disponibles en la librería de Python Seaborn.En esta ocasión se va a ver cómo construir en Python dos tipos de gráficos que pueden ser muy útiles: los mapas de calor y los diagramas de araña.
Para construir el primero de ellos se utilizará Seaborn, mientras que para el segundo se utilizará matplotlib.Saber construir mapas de calor y diagramas de araña en Python es de gran ayuda a la hora de mostrar los resultados obtenidos en nuestros análisis.
Mapas de calor con Seabourn
Un mapa de calor es una representación gráfica de los valores contenidos en una matriz mediante el uso de colores.En estos, los índices de la matriz representan las variables de dos características que se desean comparar. Mientras que el color utilizado en cada elemento de la matriz representa la magnitud de la relación existente. Siendo una herramienta excelente para mostrar las relaciones existentes entre las variables de diferentes características, ya que al mostrar la relación mediante un color se obtiene una interpretación fácil e intuitiva de esta.No solo esto, sino que al mismo tiempo se puede ver comparar las relaciones de unas características con otras observando otros puntos del mapa de calor.
Un ejemplo para crear un mapa de calor con datos aleatorios se puede ver en el siguiente trozo de código.""")

st.write("""# ![linea 2](https://i.postimg.cc/tgXw1y81/uuuu.jpg) """)

st.write("""En este código se importa inicialmente las librerías necesarias: seaborn, pandas y numpy.Una vez realizado esto se ha de crear una matriz de datos aleatoria, para lo que se utiliza el método random de numpy. Esta es la matriz que se representa, para lo que se utiliza la función heatmap de seaborn. La función únicamente necesita la matriz que contiene los valores a representar, aunque se puede indicar otros parámetros para personalizar el resultado. En el ejemplo anterior se han empleado:
center: el valor en el cual centrar el mapa de color al representar los datos.cmap: indica el mapa que se utilizará para la representación de los valores,annot: indica si se representa o no la magnitud de cada celda en el mapa además del color, por defecto no se representaráfmt: es el formato con el que se representará la magnitud.
Los resultados obtenidos con el código anterior se pueden ver en la siguiente figura.""")

st.write("""# ![linea 2](https://www.analyticslane.com/storage/2018/12/mapa-calor.png.webp) """)


 


st.write("""# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png) """)



st.write("""### 1.- Dataset """)

     
st.write(""" Para poder tener el  <strong>Datset</strong> hay que recolectar información con una encuenta elaborada por nosotros. """)


st.write("""##### Encuesta ejemplo: """) 

st.write("La encuesta la realizamos en Google-Form donde se solicitara escoger una Película.                                              Donde si escoge 1 es el que menos le gusta hasta 5 que es el que mas le gusta (escala de liker)")

st.write("### Propuesta")

expander = st.expander(" **Propuesta** ")
expander.write("# [![Captura-de-pantalla-de-2022-12-06-15-28-11.png](https://i.postimg.cc/4dc1swLG/Captura-de-pantalla-de-2022-12-06-15-28-11.png)](https://postimg.cc/CBF84Cpr)\n "" [![image.png](https://i.postimg.cc/cCqdjWMH/image.png)](https://postimg.cc/JDqwD9FV)\n "" [![image.png](https://i.postimg.cc/4NgJQJx2/image.png)](https://postimg.cc/ThtMRvmn)\n "" [![image.png](https://i.postimg.cc/8cYq7mc0/image.png)](https://postimg.cc/vxWPj9Wr)\n "" ![image.png](https://regresoseguroaclasesp.files.wordpress.com/2022/12/ssssss.jpg)\n "" ![image.png](https://regresoseguroaclasesp.files.wordpress.com/2022/12/aaaa.jpg)\n "" ![image.png](https://regresoseguroaclasesp.files.wordpress.com/2022/12/eeee.jpg)\n \n "" ![image.png](https://regresoseguroaclasesp.files.wordpress.com/2022/12/iiiii.jpg)\n " )






#Importamos librerias para Ciencia de Datos y Machine Learning
import numpy as np
import pandas as pd


st.write("### Archivo CSV separado por comas y tabla con NAN")
archiv = pd.read_csv('Pelicula.csv',
engine='python')

#leer  lineas
expander = st.expander(" **Archivo CSV** ")
expander.dataframe(archiv)
expander.write('Datos del dataframe "NAN"')
expander.dataframe(archiv.dtypes)
expander.write("### Cantidad de Filas y Columnas")
expander.dataframe(archiv.shape)




# I
# In[ ]:


archiv.isnull().sum()


st.write("""# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png) """)  

st.write("""### 2.- Correlación de Pearson  (Similitud) y Sustitución de los NAN """)  

# In[ ]:


n = archiv[archiv.columns[1:]].to_numpy()
m = archiv[archiv.columns[0]].to_numpy()


# In[ ]:




# In[ ]:
tnsp = pd.DataFrame(n.T, columns = m)
tnsp.describe()

Elim=tnsp.dropna(axis = 1, how = "all")
data_f = Elim.fillna(Elim.median(numeric_only=True))

panda_corr = data_f.corr().round(3)

expander.write(""" Haciendo la Traspuesta para ordenar la tabla """) 

expander = st.expander(" **Transpuesta** ")
expander.dataframe(tnsp)
expander.write(""" Eliminando columnas con puros NAN """)
expander.dataframe(Elim)
expander.write(" **Reemplazando valores perdidos de NAN** ")
expander.dataframe(data_f)
expander.write(" **Tabla limpia de NAN** ")
expander.dataframe(data_f)
expander.write(" **Tabla de Correlacion de PANDAS** ")
expander.dataframe(panda_corr)



tnsp.describe()





data_f.info()



# In[ ]:


panda_corr.describe()


# In[ ]:


panda_corr.isnull().sum()


# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

st.write("""### 4.- Matrix de Correlación nuestra """)


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
        
        
Listf = [round(x,3) for x in colist]


matf=np.array(Listf).reshape(40,40)



import pandas as pd

print("NumPy Data Array is:")
print(matf)

print("")
Nuestro_corr = pd.DataFrame(matf, index=lista_u, columns=lista_u)

        
expander = st.expander(" **Correlacion en Lista** ")
expander.dataframe(colist)
expander.write(" **ARRAY de la correlacion** ")
expander.dataframe(matf) 
expander.write(" **Nuestra Matriz de correlación convertida** ")
expander.dataframe(Nuestro_corr)





# ## Gráfica de Calor

# <div class="alert alert-info">
# 
#     
#    **HALLAR**: a partir de la matriz de correlación en  <strong>Pandas</strong> .
#     
#    **Instalar** : `matplotlib` `seaborn`
#     
# </div>

# In[ ]:


st.write("""### MAPA DE CALOR """)

st.write("""#### correlación de Pandas """)

st.write("""# ![linea 1](http://localhost:8501/media/88fdde77c84bfc5105bca2c4fe54c4888ba3eef2136dcdc34359009b.png)""")

st.write("""#### correlación nuestra """)
st.write("""# ![linea 1](http://localhost:8501/media/f6ad9147071cdb2b6044163caae11851698b13d787550e5f1c37387e.png)""")


st.write("""### 5.- RESULTADOS """)

st.write(""" Los resultados de similitud obtenidos en la *Encuesta de PELICULAS* según la tabla de *Correlación* con los siguientes encuestados: """)
# 
st.write("""1. _paricahuabrayan@gmail.com_ y _teleco.god@gmail.com_  obtienen el **PRIMER** indice mas alto de similitud con 0.871 """)
#  
st.write("""2. _teleco.god@gmail.com_ y _brisarakioneira@gmail.com_ obtienen el **SEGUNDO** indice mas alto de similitud con 0.773 """)


#     
st.write(""" **HALLAR**: a partir de la matriz de correlación en  Pandas. A simple vista se puede observar los resultados, pero para una matriz mas grande se debe programar una `función` o `método` para que **localice los dos usuarios con mas alto valos de correlación**. """)
#     
# </div>

st.write("""# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png) """)

st.markdown("""### Validación de Resultados """)

st.write("""# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png) """)

st.write("""### Validación - Matrix de Correlación""")


# 
st.write("""   Se debe llenar la tabla de __VALIDACIÓN de la Matriz de Correlación__ con los valores de `Similitud` obtenidos""")
#     
#     
st.write("""En `NUMPY` a partir de las matrices `n` y `m` con funciones.""")    



st.write("""### Validacion de resultados del panda""") 




st.write("""VALORES ALTOS DE SIMILITUD EN PANDAS""") 

st.write("""El 1er mayor valor de similitud es: 0.871""") 
st.write("""El 2do valor mayor despues del primero es: 0.773""")



st.write("""##### EL CORREO Y PUNTAJE CORRESPONDIENTE SON:""")
st.write("""paricahuabrayan y teleco.god     con    0.871""")
st.write("""paricahuabrayan    y
                 brisarakionera  con   0.773""")

maxim = panda_corr.unstack()
print(maxim.sort_values(ascending=False)[range(len(panda_corr),((len(panda_corr)+4)))])


st.write("""### Validacion de resultados nuestro""") 




st.write(""" VALORES ALTOS DE SIMILITUD EN NUESTRA MATRIZ DE CORRELACION""")

st.write("""El 1er mayor valor de similitud es: 0.871""") 
st.write("""El 2do valor mayor despues del primero es: 0.773""")


st.write("""##### EL CORREO Y PUNTAJE CORRESPONDIENTE SON:""")
st.write("""paricahuabrayan y teleco.god     con    0.871""")
st.write("""paricahuabrayan    y
                 brisarakionera  con   0.773""")

#EL CORREO Y PUNTAJE CORRESPONDIENTE SON:
maxim = Nuestro_corr.unstack()
print(maxim.sort_values(ascending=False)[range(len(Nuestro_corr),((len(Nuestro_corr)+4)))])


# In[ ]:


st.write("""##### Los primeros correos con mayor valor de similitud y puntaje son: \n \n paricahuabrayan y teleco.god con 0.871""")

st.write("""##### Los segundos correos con mayor valor de similitud mayor despues del primero son: \n \n brisarakionera y teleco.god con 0.773""")

# Se realiza la validación de los resultados obtenidos con la   `Matriz de Correlación de Pearson` en `Numpy` 
#  

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

st.write("""#### Conclusiones""")

#  <div class="alert alert-info">
#     
#    - ¿Se valido o no los resultados?
#    - Los resultados Validados son:
#    - ¿Es efectivo el metodo de correlación de pearson?
#    - Correlación de Pearson y Regresión Lineal, ¿cual es su relación?
#     
#  </div>

st.write("""##### ¿Son valido o no los resultados?\n
Los datos fueron sacados de una encuesta confiable,relizada por mi grupo los resultados expresados son corroborados por una serie de codigos importados de la biblioteca pandas y numpy los cuales arrojaron las posibles relaciones exitentes entre los datos ya sea su grado de similitud sus maximos y minimos ,la correlacion que exiten entre estos .etc \n

##### ¿Es efectivo el metodo de correlación de pearson?
 La correlacion de pearson sirve para calcular la la correlacion de dos datos en general se trata de 'x' y ',Para una busqueda de muchos datos esta no seria efectivo ,ya que esta destinado al uso de 2 datos,ademas que las variables que se nesesita deben ser medidads a un nivel cuantitativo continuo. Ademas la distribucion de las variables deben ser semejantes a la curva normal. A menos que buaquemos la compracion entre dos datos para ver si coinciden en difernetes aspectos \n

##### Los resultados Validados son: \n
 De acuerdo a la correlación de pandas, al igual en la misma matriz de correlacion creada por un algoritmo de nosotros los resultados obtenidos fueron los mismos, los resultados validados y con mayor similitud son:\n
 
- **Los primeros correos con mayor valor de similitud y puntaje son:** \n
  
  paricahuabrayan y teleco.god con 0.871 \n
 
- **Los segundos correos con mayor valor de similitud mayor despues del primero son:** \n
  
  brisarakionera y teleco.god con 0.773 \n
  
 con esto confirmamos que los resultados son los mismos \n

#####  Correlación de Pearson y Regresión Lineal, ¿cual es su relación? \n
 La correlacion lineal es un metodo estadistico que permite cuantificar la relacion lineal entre dos variables . El coeficiente de correlacion de Pearson es una prueba que mide la relacion estadística entre dos variables continuas ,lo cual esta ligado con la regresión lineal ya que cuentan con un rango que se establece de +1 y -1 además al igual que una regresión lineal mientras el valor de una varible aumenta la otra disminuye .
Para llevar a cabo la correlacion Pearson.
""")
st.write("# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)")
