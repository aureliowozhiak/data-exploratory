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
        
        # Read the table into a pandas DataFrame
        df = pd.read_html(str(table))[0]
        return df
