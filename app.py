import streamlit as st
import pandas as pd
from recomendador import recomendar_juegos
from etl_pagi import etl
from iniciador import inicio

def main():

    if "juegos_rating_usuario" not in st.session_state:
        st.session_state["juegos_rating_usuario"] = list()

    # Define el título de la página
    st.set_page_config(page_title='Recomendador de juegos', page_icon=':bar_chart:', layout='wide')

    menu = ["Inicio", "ETL", "Recomendador"]

    choice = st.sidebar.selectbox(label = "Menu", options = menu, index = 0)

    if choice == "Inicio":
        inicio()

    elif choice == "ETL":
        etl()

    elif choice == "Recomendador":
        recomendar_juegos()


if __name__ == "__main__":
    main()