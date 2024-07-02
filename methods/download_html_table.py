import streamlit as st

class DownloadHtmlTable:
    def __init__(self, url):
        self.url = url

    def download(self):
        import requests
        import pandas as pd
        from bs4 import BeautifulSoup

        # Download the HTML content
        response = requests.get(self.url)
        html = response.content

        # Parse the HTML content
        soup = BeautifulSoup(html, "html.parser")

        # Find the table element
        table = soup.find("table")

        # Find the number of tables in the HTML content
        tables = soup.find_all("table")

        # Get the number of tables
        number_of_tables = len(tables)

        # Select the table to convert to a pandas DataFrame
        i = st.selectbox("Selecione a tabela para converter", list(range(number_of_tables)))

        # Convert the table to a pandas DataFrame
        df = pd.read_html(str(table))[i]

        return df
