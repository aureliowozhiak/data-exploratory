import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import Utils

utils = Utils()
def upload_file():
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
            utils.view_options(df, choice)

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



def download_html_table():
    st.text('Data from HTML Table')

    url = st.text_input('Digite a URL do site')
    position = int(st.number_input('Insira a posição da sua tabela') - 1)

    df = pd.read_html(url)[position]


def main():
    utils = Utils()

    st.title("Data Engineer Helper Tool")

    menu = ['Upload File', 'Download data from HTML table']

    menu_option = st.selectbox("O que você deseja fazer?", menu)

    if menu_option == 'Upload File':
        upload_file()
    elif menu_option == 'Download data from HTML table':
        download_html_table()


if __name__ == "__main__":
    main()
