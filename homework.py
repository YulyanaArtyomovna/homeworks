import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
url=input('Enter Url')
html=requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
print(soup)
whole_text=soup.get_text()
print(whole_text)
tokens = nltk.word_tokenize(whole_text)
print(tokens)
stop_words = set(stopwords.words('english'))
filtered_html = []
for w in tokens:
       if w not in stop_words:
            filtered_html.append(w)
print(filtered_html)
