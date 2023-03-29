import streamlit as st
import pandas as pd

def recomendar_juegos():  

    st.title('Recomendador')
    st.image("https://i.gifer.com/origin/3e/3e3d17b8111c045a0e1a7835cf2b4325.gif", use_column_width=True, width=None)
    st.write("Bienvenido al recomendador de juegos personalizado. Este recomendador tiene en cuenta tus gustos y las consolas que posees, y utiliza esta información para hacer recomendaciones basadas en géneros y plataformas de compra. También tendrás la oportunidad de puntuar los juegos que has jugado previamente para que el recomendador pueda entender mejor tus preferencias. Diviértete descubriendo nuevos juegos que te encantarán")

    # carga los datos
    df = pd.read_pickle("./finaljuegos_1.pkl", compression="gzip")
    df = df.iloc[:, 1:]
    df.drop_duplicates("name", inplace=True)
    df_1 = df[["name", "background_image", "rating", "released", "tag_names", "tag_names_str"]]
    df.drop(["background_image", "rating", "released", "tag_names", "tag_names_str"], axis=1, inplace=True)

    with st.form("Consola", clear_on_submit = False):
        consolas_usuario = st.multiselect("Elige las consolas que poseas:", options=df.columns[2:28])
        st.form_submit_button(label='Submit')


    col1, col2 = st.columns([1, 1])
    juego = col1.selectbox("Elige un juego que hayas jugado:", options=df["name"])
    rating = col2.slider(f"¿Qué valor le das a '{juego}' del 1 al 5?", 1, 5)

    if st.button("Agregar juego"):
       
        st.session_state["juegos_rating_usuario"].append([juego, rating])


    no_consolas = ['name', 'playtime','Action','Adventure','Arcade','Board Games','Card','Casual','Educational',
                    'Family','Fighting','Indie','Massively Multiplayer','Platformer','Puzzle','RPG','Racing','Shooter',
                    'Simulation','Sports','Strategy','App Store','Epic Games','GOG','Google Play','Nintendo Store',
                    'PlayStation Store','Steam','Xbox 360 Store','Xbox Store','Multiplayer','Singleplayer']

    columnas_final = no_consolas + consolas_usuario

    juegos_usuario = pd.DataFrame(st.session_state["juegos_rating_usuario"], columns=["name", "rating"]).drop_duplicates()
    st.write(juegos_usuario)

    juegos_matriz = df[~df["name"].isin(juegos_usuario["name"])][columnas_final]

    for col in consolas_usuario:
        juegos_matriz = juegos_matriz[juegos_matriz[col] == 1]


    if juegos_matriz.empty:
        return "No hay juegos recomendados para estas consolas."

    df_usuario = df[df["name"].isin(juegos_usuario["name"].to_list())]

    weighted_genre_matrix = (df_usuario.iloc[:, 1:].values.T * juegos_usuario["rating"].values).T

    weighted_genre_matrix = weighted_genre_matrix.sum(axis=0)

    user_input = pd.DataFrame.from_dict({col: [val] for col, val in zip(df.columns[1:], weighted_genre_matrix)})[columnas_final[1:]]

    user_input = user_input / user_input.sum(axis=1)[0]

    df_recom = pd.DataFrame()

    df_recom["name"] = juegos_matriz["name"]
    df_recom["valor"] = (juegos_matriz.iloc[:, 1:].values * user_input.values).sum(axis=1)

    df_recom = df_recom.head(40)

    df_recom = pd.merge(left = df_recom, right = df_1, on = "name", how = "inner").drop_duplicates()

    st.write(df_recom.sort_values("valor", ascending = False).reset_index(drop = True))
