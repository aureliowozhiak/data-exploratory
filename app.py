import streamlit as st
import pandas as pd

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

            # Adicione um botão para criar um gráfico de barras com a contagem de valores de uma coluna
            # Se clicar no botão, mostre um selectbox com as colunas do dataframe
            # Se o usuário escolher uma coluna, mostre o gráfico de barras
            # Use o st.pyplot() para mostrar o gráfico
            # Use também o método value_counts() do pandas para contar os valores da coluna
            

        except Exception as e:
            st.write("Erro ao ler arquivo CSV")
            st.write(e)

if __name__ == "__main__":
    main()
