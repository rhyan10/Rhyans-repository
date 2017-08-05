from bs4 import BeautifulSoup as bs
import urllib2,lxml,urlparse,sys
import MySQLdb as sql
import pandas as pd

try:
    db = sql.connect(host="192.168.1.23",port= 3306,user ="Dataspartan", passwd = "littledataspartan", db = "stock")

    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    results = cursor.fetchone()
    # Check if anything at all is returned
    if results:
        print "connected"
        # return True
    else:
        print "didn't connect"
        # return False
except MySQLdb.Error:
    print "ERROR IN CONNECTION"

def remove_nasdaq():
    '''
    removes the unwanted data from the csv
    '''
    symbol = row.find(text = True)
    if "NASDAQ" not in symbol:
        symbols.append(symbol)
    else:
        pass
    return symbol
    
def create_sql_table():
    stockdb = db.cursor()
    sqlcode = """ CREATE TABLE StockDataa (StockId VARCHAR(10),daate VARCHAR(9),Open FLOAT,High FLOAT,Low FLOAT,Close FLOAT,Volume BIGINT); """
    stockdb.execute(sqlcode)
        for name in symbols:
            csvlink = "http://www.google.co.uk/finance/historical?q=NASDAQ%3A"+name+"&start=0&num=31&output=csv"
            mycsvfile = pd.read_csv(csvlink)

def get_csv():
    r = urllib2.urlopen('http://www.nasdaq.com/markets/most-active.aspx').read()
    soup = bs(r, 'lxml')
    symbols = []
    for row in soup.findAll('h3'):
        remove_nasdaq()





    #print(mycsvfile)
    #for row in mycsvfile:
	 #      stockdb.execute("INSERT INTO cycling(StockId,Date,Open,High,Low,Close,Volume) VALUES(%s, %s, %s, %s, %s, %s, %s)", row)


#names = soup.find_all('h3')
#print(pd.read_csv('http://www.google.co.uk/finance/historical?q=NASDAQ%3AGOOGL&start=30&num=30&output=csv'))
