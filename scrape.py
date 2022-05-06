from bs4 import BeautifulSoup
import requests as r
import pandas as pd


response = r.get('https://www.teenvogue.com/gallery/best-harry-potter-quotes')
content = response.text
soup = BeautifulSoup(content, 'html.parser')

olTags = soup.find_all('ol')
all_quotes = []
for idx, tags in enumerate(olTags):
    for quote in olTags[idx]:
        line = quote.text
        line = line.encode('ascii', 'ignore').decode('ascii')
        all_quotes.append(line)

df = pd.DataFrame({'Quotes' : all_quotes})
df.to_csv('HarryPotter_quotes.csv', index = False)




    



