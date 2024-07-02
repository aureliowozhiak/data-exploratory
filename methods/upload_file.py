import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from methods.utils import Utils

utils = Utils()


class UploadFile:
    def __init__(self):
        pass

    def upload_file(self):
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
                
                '''col_choice = st.selectbox("Selecione a coluna para contagem de valores", df.columns)
                tipo = st.selectbox('Selecione o tipo do gráfico', ['bar', 'area', 'line', 'pie'])
                if col_choice:
                    if st.button('Criar gráfico de barras'):
                        fig, ax = plt.subplots()
                        df[col_choice].value_counts().plot(kind=tipo, ax=ax)
                        st.pyplot(fig)'''

                xchoice = st.selectbox('Selecione a coluna com os dados para x', df.columns)
                ychoice = st.selectbox('Selecione a coluna com os dados para y', df.columns)
                tipo = st.selectbox('Selecione o tipo do gráfico', ['bar', 'area', 'line', 'pie'])
                if ychoice and xchoice:
                    fig, ax = plt.subplots()
                    if tipo == 'bar':
                        ax.bar(df[xchoice], df[ychoice])
                        ax.set_xlabel(xchoice)
                        ax.set_ylabel(ychoice)
                        ax.set_title('Gráfico de Barras')
                    
                    elif tipo == 'area':
                        ax.fill_between(df[xchoice], df[ychoice])
                        ax.set_xlabel(xchoice)
                        ax.set_ylabel(ychoice)
                        ax.set_title('Gráfico de Área')
                    
                    elif tipo == 'line':
                        ax.plot(df[xchoice], df[ychoice])
                        ax.set_xlabel(xchoice)
                        ax.set_ylabel(ychoice)
                        ax.set_title('Gráfico de linha')

                    elif tipo == 'pie':
                        ax.pie(df[ychoice], labels=df[xchoice], autopct='%1.1f%%')
                        ax.set_title('Gráfico de Pizza')
                    
                    st.pyplot(fig)

            except Exception as e:
                st.write("Erro ao ler arquivo CSV")
                st.write(e)
