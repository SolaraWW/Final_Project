
import urllib2
mydata = urllib2.urlopen('https://www.quandl.com/api/v3/datasets/NASDAQ/AAPL_NET_INC.csv?api_key=WiJ7yFp1hjJaX77v1DZs').read()
print mydata
