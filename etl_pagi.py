import streamlit as st
import pandas as pd

def etl():
    df = pd.read_csv("C:/Users/Fgonz/Documentos/Repositorios/Moviles/Streamlit/streamlit-env/df_streamlit.csv")
     # Define las opciones del menú
    options_etl = ["Explicación","Visualizaciones", "Herramientas"]
    # Agregar subopciones dentro de la pestaña ETL
    choice_etl = st.sidebar.selectbox("Seleccione una opción", options_etl)

    if choice_etl == "Explicación":
        st.write("En primer lugar, se utilizaron datos obtenidos de la API de Rawg y se realizaron tareas de transformación y limpieza de datos para seleccionar las características más importantes de cada juego y representarlas de manera adecuada en un DataFrame.")
        st.write("Posteriormente, se transformó el DataFrame para incluir 63 columnas de 0s y 1s, lo que permitió entrenar el modelo del recomendador para proporcionar recomendaciones precisas a los usuarios.")
        st.write("La transformación de datos fue un proceso meticuloso y detallado que implicó el uso de técnicas avanzadas de análisis de datos y aprendizaje automático para garantizar la precisión y la calidad de los datos. ¡Gracias a este proceso, se pudo crear un recomendador de juegos eficaz y preciso para ayudar a los usuarios a descubrir nuevos juegos que se ajusten a sus gustos y preferencias! Y este es el dataframe resultante:")
        st.dataframe(df)
    if choice_etl == "Visualizaciones":
        st.write("La primera gráfica contabiliza los juegos por género, lo que permite a los usuarios visualizar cuántos juegos están disponibles en cada categoría. Esta información puede ser útil para aquellos que quieren descubrir juegos nuevos que se ajusten a sus intereses.")
        st.write("La segunda gráfica cuenta los juegos por número de jugadores, lo que ayuda a los usuarios a identificar juegos que son adecuados para su grupo de amigos o familia. Por ejemplo, si estás buscando un juego para jugar con amigos, esta gráfica puede ayudarte a encontrar opciones que sean divertidas para un grupo grande de personas.")
        st.write("La tercera gráfica contabiliza los juegos por plataforma, lo que es especialmente útil para aquellos que quieren encontrar juegos que sean compatibles con su consola o dispositivo de juego. Esta información te permitirá ver rápidamente cuántos juegos están disponibles en cada plataforma.")
        st.write("Por último, la cuarta gráfica cuenta los juegos por tienda online, lo que es útil para aquellos que buscan encontrar juegos disponibles en una tienda específica. Esta gráfica te permitirá ver cuántos juegos están disponibles en cada tienda en línea y hacer una selección informada sobre dónde comprar tus juegos.")
        # URL de Power BI
        st.markdown(body= '<iframe title="Visual - Página 1" width="1000" height="960" src="https://app.powerbi.com/view?r=eyJrIjoiYTM5YTFkNTctMTVjNS00MDM0LWJjMDQtZTJhZWVmYzJkYzYzIiwidCI6ImQ0NmI5YmZiLTRjYzYtNGJmYy1hYTFjLWM2MzIxNTg1ZGNiNSIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>',
                    unsafe_allow_html= True)

    elif choice_etl == "Herramientas":
        col1, col2 = st.columns([1, 1])
        col1.image("https://mms.businesswire.com/media/20200616005364/en/798639/23/Streamlit_Logo_%281%29.jpg", use_column_width=True, width=None)
        col2.write("En primer lugar, se utilizó Jupyter Notebook, una herramienta popular en el mundo de la ciencia de datos, para realizar el ETL y el EDA de los datos de juegos obtenidos de la API de Rawg. Jupyter Notebook es una herramienta que permite a los científicos de datos y programadores explorar, analizar y visualizar datos en un entorno interactivo.")
        col2.write("En segundo lugar, se utilizó Streamlit, una herramienta de desarrollo de aplicaciones web para Python, para diseñar la página de recomendaciones de juegos. Streamlit permite a los desarrolladores crear fácilmente aplicaciones web interactivas con Python y presenta una interfaz intuitiva para el usuario final.")
        col2.write("Por último, se utilizó Power BI, una herramienta de visualización de datos de Microsoft, para crear las gráficas y visualizaciones de datos utilizadas en el proyecto. Power BI es una herramienta que permite a los usuarios crear gráficas y visualizaciones interactivas y personalizadas utilizando datos de múltiples fuentes.")