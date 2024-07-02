from methods.download_html_table import DownloadHtmlTable
from methods.upload_file import UploadFile
import streamlit as st

def main():

    st.title("Data Engineer Helper Tool")

    menu = ['Upload File', 'Download data from HTML table']

    menu_option = st.selectbox("O que você deseja fazer?", menu)

    match menu_option:
        case 'Upload File':
            UF = UploadFile()
            UF.upload_file()
        case 'Download data from HTML table':
            # https://en.wikipedia.org/wiki/Python_(programming_language) by default
            #url = st.text_input("Digite a URL do site: ")
            url = st.text_input("Digite a URL do site: ", "https://en.wikipedia.org/wiki/Python_(programming_language)")
            if st.button("Download"):
                DHT = DownloadHtmlTable(url)
                df = DHT.download()
                st.write(df)


if __name__ == "__main__":
    main()
