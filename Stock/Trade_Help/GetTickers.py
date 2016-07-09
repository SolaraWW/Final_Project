import urllib2
from bs4 import BeautifulSoup
nasDaq = []
url = urllib2.urlopen('http://eoddata.com/stocklist/NASDAQ/B.htm').read()
soup = BeautifulSoup(url,"html.parser")

for a in soup.find_all('a', text=True):
    if a.text.isupper():
        if a.text.startswith('B'):
            if a.text != 'AIQ':
                nasDaq.append(a.text.strip())

print nasDaq
