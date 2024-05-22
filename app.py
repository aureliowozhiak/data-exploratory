import streamlit as st
import pandas as pd

def main():
    # titulo
    st.title("Opa!")

    # descrição
    st.text('''     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et dui turpis.
    Nulla eu dolor ac magna iaculis tempus. Mauris quis metus tortor.
    Pellentesque ac pulvinar lectus, vel blandit erat.''')

    # botão
    if st.button("Carregar dados"):
        st.title("Dados carregados!")
    
    # exemplos pra tabela
    data = {
    'Nome': ['Alice', 'Pablo', 'Carlos'],
    'Idade': [24, 27, 15]
}

    # converter para dataframe
    df = pd.DataFrame(data)

    # mostrando tabela
    st.table(df)

if __name__ == "__main__":
    main()