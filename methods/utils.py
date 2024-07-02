import streamlit as st
class Utils:
    def __init__(self):
        pass

    def view_options(self, df, choice):
        if choice == 'Primeiras linhas':
            st.write(df.head())
        elif choice == 'Últimas linhas':
            st.write(df.tail())
        elif choice == 'Ver tudo':
            st.write(df)
        elif choice == 'Colunas':
            st.write(df.columns)
        elif choice == 'Número de linhas/colunas':
            st.write(df.shape)
        elif choice == 'Mostrar números':
            st.write(df.describe())
        elif choice == 'Tipo de dados':
            st.write(df.dtypes)
        elif choice == 'Linha aleatória':
            st.write(df.sample())