import streamlit as st
import pandas as pd

def main():
    st.title("Data Engineer Helper Tool")

    st.text('''     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et dui turpis.
    Nulla eu dolor ac magna iaculis tempus. Mauris quis metus tortor.
    Pellentesque ac pulvinar lectus, vel blandit erat.''')

    uploaded_file = st.file_uploader("Carregue um arquivo CSV", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Arquivo carregado com sucesso!")

            # Ver primeiras linhas (usando a função head)
            if st.checkbox("Mostrar primeiras linhas"):
                st.write(df.head())

            # Ver últimas linhas
            # Crie um checkbox para mostrar as últimas linhas (dica use a função tail)
            #
            #
            #

            # Ver tudo
            if st.checkbox("Mostrar tudo"):
                st.write(df)

            # Ver colunas
            # Crie um checkbox para mostrar as colunas do dataframe (dica use a função columns)
            #
            #

        except Exception as e:
            st.write("Erro ao ler arquivo CSV")
            st.write(e)

if __name__ == "__main__":
    main()
