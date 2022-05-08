import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.hypable.com/best-harry-potter-quotes-books-movies/')
soup = BeautifulSoup(response.text, 'html.parser')

divTag = soup.find_all("ol")

lst = []
for line in divTag:
    row = line.text
    lst.append(row)

df = pd.DataFrame({"quote": lst})
df.to_csv('HarryPotterQuotes2.csv')