import streamlit as st
import pandas as pd

def main():
    # titulo do app
    st.title("Data Engineer Helper Tool")

    # descrição do app
    st.text('''     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et dui turpis.
    Nulla eu dolor ac magna iaculis tempus. Mauris quis metus tortor.
    Pellentesque ac pulvinar lectus, vel blandit erat.''')

    uploaded_file = st.file_uploader("Carregue um arquivo CSV", type="csv")


    # if a file is uploaded, read it and display it
    if uploaded_file is not None:
        # ler content do arquivo
        try:
            df = pd.read_csv(uploaded_file)
            st.write(df)
        except Exception as e:
            st.write("Erro ao ler arquivo CSV")
            st.write(e)
            
if __name__ == "__main__":
    main()