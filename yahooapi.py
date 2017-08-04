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
for name in symbols:
    csvlink = "http://www.google.co.uk/finance/historical?q=NASDAQ%3A"+name+"&start=0&num=31&output=csv"
    sqlcode = """ CREATE TABLE """ + name """ (
    Date VARCHAR(9)
    Open FLOAT
    High FLOAT
    Low FLOAT
    Close FLOAT
    Volume BIGINT); """
    stockdb.execute('CREATE TABLE ' + name)
    #print csvlink

#names = soup.find_all('h3')
print(pd.read_csv('http://www.google.co.uk/finance/historical?q=NASDAQ%3AGOOGL&start=30&num=30&output=csv'))
