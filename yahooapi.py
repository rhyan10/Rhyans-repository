from bs4 import BeautifulSoup as bs
import urllib2,lxml,urlparse,sys
import MySQLdb as sql
import pandas as pd
db = sql.connect(host="127.0.0.1",user ="Dataspartan", passwd = "littledataspartan", db = "stock")
r = urllib2.urlopen('http://www.nasdaq.com/markets/most-active.aspx').read()
soup = bs(r)
symbols = []
for row in soup.findAll('h3'):

    symbol = row.find(text = True)
    if "NASDAQ" not in symbol:
        symbols.append(symbol)
    else:
        pass
stockdb = db.cursor()
sqlcode = """ CREATE TABLE StockDataa (StockId VARCHAR(10),daate VARCHAR(9),Open FLOAT,High FLOAT,Low FLOAT,Close FLOAT,Volume BIGINT); """
stockdb.execute(sqlcode)
for name in symbols:
    csvlink = "http://www.google.co.uk/finance/historical?q=NASDAQ%3A"+name+"&start=0&num=31&output=csv"
    mycsvfile = pd.read_csv(csvlink)
    #print(mycsvfile)
    #for row in mycsvfile:
	 #      stockdb.execute("INSERT INTO cycling(StockId,Date,Open,High,Low,Close,Volume) VALUES(%s, %s, %s, %s, %s, %s, %s)", row)


#names = soup.find_all('h3')
#print(pd.read_csv('http://www.google.co.uk/finance/historical?q=NASDAQ%3AGOOGL&start=30&num=30&output=csv'))
