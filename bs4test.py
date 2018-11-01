from bs4 import BeautifulSoup
from nltk.tokenize import TweetTokenizer
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#Parse HTML text 
soup = BeautifulSoup(html_doc, 'html.parser')
#Find all links
links = soup.find_all('a')
#Extract text from HTML
text = soup.get_text()

#Print out set of links
for i in links:
    print (i.get('href'))

#Use a tweet tokenizer from NLTK package
tknzr = TweetTokenizer()
#Get rid of semicolons and other punctuations? Not sure if this is important. 

#Tokenize Text
print(tknzr.tokenize(text))

##Extracting wikipedia links from google 
'''
links1 = []
#Tokenize into 'get' query formats 
query = 'Lebron James'
query = urllib.parse.quote_plus(query)

#Get request to a link; return status code 200 if successful. r.text has all the text saved
r = requests.get('https://www.google.com/search?q=site:wikipedia.com+{}&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw'.format(query))

#Convert it to a soup object, but parsing it usin html so it understands the text being parsed. 
soup = BeautifulSoup(r.text, "html.parser")

for item in soup.find_all('h3', attrs={'class' : 'r'}):
    links1.append(item.a['href'][7:])
'''