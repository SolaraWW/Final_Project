import quandl
mydata = quandl.get_table('ZACKS/FC', ticker='AAPL')
print mydata
