import streamlit as st
import pandas as pd

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
            # Ver primeiras linhas (usando a função head)
            if choice == 'Primeiras linhas':
                st.write(df.head())

            # Ver últimas linhas
            # Crie um checkbox para mostrar as últimas linhas (dica use a função tail)
            if choice == 'Últimas linhas':
                st.write(df.tail())
            
            # Ver tudo
            if choice == 'Ver tudo':
                st.write(df)

            # Ver colunas
            # Crie um checkbox para mostrar as colunas do dataframe (dica use a função columns)
            if choice == 'Colunas':
                st.write(df.columns)

            # Pesquisar outras funções para vizualização de tabela (describe)
            # Ver uma linha aleátoria
            if choice == 'Linha aleatória':
                st.write(df.sample())
            
            # Número de linhas e número de colunas
            if choice == 'Número de linhas/colunas':
                st.write(df.shape)

            # Estatistícas númericas das colunas
            if choice == "Mostrar números":
                st.write(df.describe())

            # Exibir o tipo de dados de cada coluna
            if choice == "Tipo de dados":
                st.write(df.dtypes)


        except Exception as e:
            st.write("Erro ao ler arquivo CSV")
            st.write(e)

if __name__ == "__main__":
    main()
