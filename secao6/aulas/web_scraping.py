import requests
from bs4 import BeautifulSoup
import os

os.system('cls')

url = 'https://www.otaviomiranda.com.br'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(url, headers=headers)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

print(parsed_html.section.text)