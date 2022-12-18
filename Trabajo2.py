
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px
import io 




with st.sidebar:
    choose = option_menu("Aplicación en IA  Sistema Recomendador ", ["About", "Photo Editing", "Project Planning", "Python e-Course", "Contact"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#FFFFFF"},
        "icon": {"color": "Green", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#A9A9A9"},
        "nav-link-selected": {"background-color": "#000000"},
    }
    )


logo = Image.open('unsa.png')
if choose == "About":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Universidad Nacional San Agustin de Arequipa</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    st.write("Hola y bienvenidos") 
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