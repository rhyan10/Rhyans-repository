import logging
import os
from flask import Flask
import json
from flask_ask import Ask, request, session, question, statement
state = 0
variable = None
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
from query import Queries
from Classes import calculus,functions,ApiConnect
from stockssqldatabase import database
cal = calculus()
connect = ApiConnect()
func = functions()
Quack = Queries()
data = database()
@ask.launch
def lauchmessage():
    return question("Hello mee Pablo errrrrrrrrrr. What would you like to ask!").reprompt("Didn't get that. Could you please repeat?")
@ask.intent('averagepriceintent')
def price(companyname):
    ticker = Quack.getdict(companyname)
    answer = Quack.totalaverage(ticker)
    price = float(answer[0][0])
    price = round(price,1)
    price = str(price)
    return question("The average share price of {} is {}".format(companyname,price))
@ask.intent('IndefiniteIntIntegralIntent',convert={'a':int, 'b':int, 'c':int, 'd':int, 'e':int})
def integrate(a,b,c,d,e):
    speech_text = cal.Integralindef(a,b,c,d,e)
    return question(speech_text)
@ask.intent("MaximumColumnValueIntent")
def max_min_value(start_date, end_date, companyname, function, valuetype):
    ticker = Quack.getdict(companyname)
    answer = Quack.simplefunctions(ticker,function,valuetype, data.changingyear(start_date), data.changingyear(end_date))
    return question("The " + str(function) + " " + str(valuetype) + " price between " + data.changingyear(start_date) + " and " + data.changingyear(end_date) +" for " + companyname + " is " + str(round(float(answer[0][0]),1)))
@ask.intent("StandardIntent")
def getstandard(companyname):
    ticker = Quack.getdict(companyname)
    return question("The standard deviation of {} is {}".format(companyname,str(round(float(Quack.getdeviation(ticker)[0][0]),1))))
@ask.intent("DataOperationIntent")
def get_ticker(start_date, end_date, companyname, function):
    ticker = Quack.getdict(companyname)
    if function == 'average':
        answer = round(Quack.avg_shares(ticker, data.changingyear(start_date), data.changingyear(end_date)),1)
        return question("The " + str(function) + " shares price between " + data.changingyear(start_date) + " and " + data.changingyear(end_date) + " is " + str(round(float(answer[0][0]),1)))
    elif function == 'minimum':
        answer = round(Quack.min_shares(ticker, data.changingyear(start_date), data.changingyear(end_date)),1)
        return question("The " + str(function) + " shares price between " + data.changingyear(start_date) + " and " + data.changingyear(end_date) + " is " + str(round(float(answer[0][0]),1)))
    elif function == 'maximum':
        answer = round(Quack.max_shares(ticker, data.changingyear(start_date), data.changingyear(end_date)),1)
        return question("The " + str(function) + " shares price between " + data.changingyear(start_date) + " and " + data.changingyear(end_date) + " is " + str(round(float(answer[0][0]),1)))
    else:
        return question("Sorry something went wrong ask me again")
@ask.intent('VolatilityIntent')
def volatile(vol):
    if vol == 'most':
        myresult = Quack.mostvolatile()
        return question("The most risky or volatile shares to buy are from "+myresult )
    if vol == 'least':
        myresult = Quack.leastvolatile()
        return question("The least risky or volatile shares to buy are from "+myresult)

@ask.intent('firstderivative', convert={'a':int, 'b':int, 'c':int, 'd':int, 'e':int})
def differentiate(a,b,c,d,e):
    speech_text = cal.differential(a,b,c,d,e)
    global state,variable
    state = 1
    variable = speech_text.split(" ")
    return question(speech_text)
@ask.intent('AreundercurveIntent',convert={'a':int, 'b':int, 'c':int, 'd':int, 'e':int, 'start':int, 'finish':int})
def areacurve(a,b,c,d,e):
    myfunction = func.createfunctions(a,b,c,d,e)
    print (myfunction)
@ask.intent('SubtractionIntent', convert = {'a':int, 'b':int})
def subtract(a,b):
    c = a - b
    return question("{} subtract {} equals {}".format(a,b,c))
@ask.intent('MultiplyIntent', convert = {'a' :int, 'b':int })
def multiplication(a,b):
    c = a * b
    return question("{} times by {} equals {}".format(a,b,c))
@ask.intent('DivideIntent', convert = {'a':int, 'b':int})
def division(a,b):
     c = a/b
     return question("{} divided by {} equals {}".format(a,b,c))
@ask.intent('AddIntent', convert = {'a':int, 'b':int})
def addition(a,b):
     c = a+b
     return question("{}  plus {} equals {}".format(a,b,c))
@ask.intent('TweetIntent')
def calltweet(name):
    newname = name.lower().replace(" ","")
    tweet = connect.twitterconnect(newname)
    return question("The most recent tweet from {} is : {}".format(name,tweet)+". Would you like to ask something else?")
@ask.intent('YesIntent')
def yesintent():
    global variable
    if state == 1: # this will allow the user to differentiate the function as many times as they want
        mylist = []
        for listmember in variable:
            if(listmember.isdigit()==True):
                mylist.append(listmember)
            else:
                pass
        length = len(mylist)
        if length == 2 or length == 3:
             speech_text = cal.differential(int(mylist[1]),None,None,None,None)
             variable = speech_text.split(" ")
             return question(speech_text)
        elif length == 5:
            speech_text = cal.differential(int(mylist[3]),int(mylist[4]),None,None,None)
            variable = speech_text.split(" ")
            return question(speech_text)
        elif length == 7:
            speech_text = cal.differential(int (mylist[4]), int(mylist[5]), int (mylist[6]),None,None)
            variable = speech_text.split(" ")
            return question(speech_text)
        else:
            speech_text = cal.differential(int(mylist[5]),int(mylist[6]),int(mylist[7]),int(mylist[8]),None)
            variable = speech_text.split(" ")
            return question(speech_text)
@ask.intent('HelloWorldIntent', convert = {'a':int})
def hello_word(a):
       print session.attributes
       print request
       speech_text = "Hi, would you like to ask something"
       state = 5
       print a
       return question(speech_text).simple_card("Hello word", speech_text)
@ask.intent('stopintent')
def stop():
    return statement('Ok')
@ask.intent('lesliefact')
def leslie():
    return question('Women')
@ask.intent('leslieno')
def leslie():
    return question('no, he is trying too hard but he can not find. But I am available for him hehe')
@ask.intent('fanon')
def leslie():
    return question(    'Banana')
@ask.intent('fanono')
def leslie():
    return question('No, fan eat your Banana')
@ask.intent("AMAZON.NoIntent")
def nointent():
        speech_text = "ok bye"
        return statement(speech_text)
    # pass
@ask.session_ended
def session_ended():
	return "{}", 200



if __name__ == '__main__':
	app.run(debug = True)
