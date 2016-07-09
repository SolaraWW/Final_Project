import urllib2

print urllib2.urlopen('http://marketdata.websol.barchart.com/getProfile.csv?key=30620da4856af86f3138c1991b8cee29&symbol=AAU&type=yearly&startDate=20150707000000').read()
