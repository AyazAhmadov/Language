import requests
from bs4 import BeautifulSoup

html = requests.get('https://1000mostcommonwords.com/1000-most-common-german-words/').text

soup = BeautifulSoup(html, 'html.parser')

trs = soup.find_all('tr')

words = []

for i, tr in enumerate(trs):
    if i != 0:
        tds = tr.find_all('td')
        word = ','.join([td.text for i, td in enumerate(tds) if i != 0])
        words.append(word)

with open('words.csv', 'w', encoding='utf-8') as f:
    f.write('\n'.join(words))