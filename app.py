import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def view_options(df, choice):
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

def main():
    st.title("Data Engineer Helper Tool")

    st.text('''     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et dui turpis.
    Nulla eu dolor ac magna iaculis tempus. Mauris quis metus tortor.
    Pellentesque ac pulvinar lectus, vel blandit erat.''')
    sep = st.text_input('Digite qual vai ser o separador: ')
    uploaded_file = st.file_uploader("Carregue um arquivo CSV", type="csv")
    
    options = ['Ver tudo', 'Primeiras linhas', 'Últimas linhas', 'Mostrar números', 
                'Tipo de dados', 'Colunas', 'Número de linhas/colunas', 'Linha aleatória']

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, sep = sep)
            st.write("Arquivo carregado com sucesso!")
            choice = st.selectbox("Selecione o que quer vizualizar", options)
            view_options(df, choice)

            # Funções de limpeza de dados
            st.subheader("Limpeza de Dados")
            if st.button("Remover Duplicados"):
                df.drop_duplicates(inplace=True)
                st.write("Dados duplicados removidos.")
                st.write(df)
            
            # Funções valores nulos
            null_option = st.selectbox("Selecione uma coluna para tratar valores nulos", ['Todas'] + list(df.columns))
            if st.button("Remover Valores Nulos"):
                if null_option == 'Todas':
                    df.dropna(inplace=True)
                else:
                    df.dropna(subset=[null_option], inplace=True)
                st.write(f"Valores nulos removidos na coluna {null_option}.")
                st.write(df)

            col_choice = st.selectbox("Selecione a coluna para contagem de valores", df.columns)
            tipo = st.selectbox('Selecione o tipo do gráfico', ['bar', 'area', 'line', 'pie'])
            if col_choice:
                if st.button('Criar gráfico de barras'):
                    fig, ax = plt.subplots()
                    df[col_choice].value_counts().plot(kind=tipo, ax=ax)
                    st.pyplot(fig)

        except Exception as e:
            st.write("Erro ao ler arquivo CSV")
            st.write(e)

if __name__ == "__main__":
    main()
