import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.hypable.com/best-harry-potter-quotes-books-movies/')
soup = BeautifulSoup(response.text, 'html.parser')

olTags = soup.find_all('ol')
all_quotes = []

for idx, tags in enumerate(olTags):
    for quote in olTags[idx]:
        line = quote.text
        line = line.encode('ascii', 'ignore').decode('ascii')
        all_quotes.append(line)

df = pd.DataFrame({'Quotes' : all_quotes})
df.to_csv('HarryPotter_quotes2.csv', index = False)