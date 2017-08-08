from bs4 import BeautifulSoup as bs
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import urllib2,lxml,urlparse,sys
import MySQLdb as sql
import pandas as pd
import math
import datetime
import logging
import os
import time

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return 'nothing'

def connection_check():
    try:
        global db
        db = sql.connect(host="192.168.1.23",port= 3306,user ="Dataspartan", passwd = "littledataspartan", db = "stock")

        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        results = cursor.fetchone()
        # Check if anything at all is returnedeck():
        if results:
            return "######### ######### Connection Established ######### #########"
            # return True
        else:
            return "######### ######### Connection Failed To Establish ######### #########"
            # return Falseimport request
    except MySQLdb.Error:
        return "######### ######### Exception Triggered ######### Error In Connection ######### #########"

print connection_check()

def avg_of_open(end_date, start_date):
    stockdb = db.cursor()
    sql = "SELECT AVG(Open) FROM stockdata WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (end_date, start_date))
    result = stockdb.fetchall()
    db.commit()
    return result

def avg_of_high(end_date, start_date):
    stockdb = db.cursor()
    sql = "SELECT AVG(high) FROM stockdata WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (end_date, start_date))
    result = stockdb.fetchall()
    db.commit()
    return results

def avg_of_low(end_date, start_date):
    stockdb = db.cursor()
    sql = "SELECT AVG(low) FROM stockdata WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (end_date, start_date))
    result = stockdb.fetchall()
    db.commit()
    return result

def avg_of_close(end_date, start_date):
    stockdb = db.cursor()
    sql = "SELECT AVG(close) FROM stockdata WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (end_date, start_date))
    result = stockdb.fetchall()
    db.commit()
    return result

def avg_of_volume(end_date, start_date):
    stockdb = db.cursor()
    sql = "SELECT AVG(volume) FROM stockdata WHERE daate BETWEEN %s AND %s"
    stockdb.execute(sql, (end_date, start_date))
    result = stockdb.fetchall()
    db.commit()
    return result

print avg_of_open(datetime.date(2017, 02, 12), datetime.date(2017, 04, 15))
