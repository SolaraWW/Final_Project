import re

handle = 'NYSE.txt'
fh = open(handle).read()

NYSE = []

tickers = re.findall(r'[A-Z]+[A-Z]', fh)
otherTickers = re.findall(r'[A-Z]+[A-Z]*\s', fh)
NYSE.append(tickers)
#if otherTickers not i


#print tickers
print otherTickers
