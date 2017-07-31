import logging
import os
from time import gmtime, strftime
from googlefinance import getQuotes
from flask import Flask
import json
from flask_ask import Ask, request, session, question, statement
import datetime
from yahoo_finance import Share
import urllib2
state,p,q,r = 0,0,0,0 # defined here
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

class calculus:
    def integrate(self,a,b,c,state):
        if state == 0:#quadratic
            state,z,y,x = 2,a/3,b/2,c
            speech = "The integral of {} x squared {} x plus {} is {} x cubed {} x squared plus {} x, to one significant figure, would you like me to integrate that again".format(a,b,c,z,y,x)
            return(speech)
    def differential2(self,a,b,c,state):
        if state == 0:
            global z
            state,z,y = 1, a *2,b
            speech = "The first derivative of {} x squared plus {} x plus {} is {} x plus {}, would you like to differentiate that again".format(a,b,c,z,y)
            return(speech)
        if state == 1:
            z = a*2
            return ("The second derivative of {} x squared plus {} x plus {} is {}".format(a,b,c,z))
@ask.launch
def launch():
    speech_text = 'Hello , what can I do for you?'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
@ask.intent('IntegrateIntent', convert = {'a':int, 'b':int, 'c':int})
def integrat(a,b,c):
    clas = calculus()
    speech_text = clas.integrate(a,b,c,0)
    return question(speech_text)
    global p,q,r
    p,q,r = a,b,c
@ask.intent('DifferIntent', convert={'a':int, 'b':int, 'c':int})
def differentiate(a,b,c):
    clas = calculus()
    speech_text = clas.differential2(a,b,c,0)
    return question(speech_text)
    dump.write("a = {}, b = {}, c = {}".format(a,b,c)) #variables updated here ------------------------
@ask.intent('YesIntent')
def yes():
    clas = calculus()
    if state == 0: # this will differentiate it again
        clas = calculus()
        speech_text = clas.differential2(p,q,r,1) # call upon the variables
        return question(speech_text)
































@ask.intent('AddIntent', convert={'x': int, 'y': int})
def add(x, y):
    z = x + y
    return statement('{} plus {} equals {}'.format(x, y, z))
#def differentiate()
@ask.intent('HelloWorldIntent')
def hello_word():
       speech_text = "Hello there"
       return question(speech_text).simple_card('HelloWorld',speech_text)
@ask.intent('StockIntent')
def stocks():
     yahoo = Share('YHOO')
     share = yahoo.get_price()
     print(yahoo)
     print(share)
     speech_text = "The shares price of yahoo is "+ share
     return question(speech_text).simple_card('HelloWorld', speech_text)
@ask.intent('StopIntent')
def stop():
    return statement("Alright I will stop then")
@ask.intent('NoIntent')
def no():
        speech_text = "Sorry I do not understand. Please could you repeat"
        return question(speech_text).simple_card('HelloWorld',speech_text)
        #return statement("She better make it them")
@ask.intent('TimeIntent')
def time():
    if state != 5:
        speech_text = "Sorry I do not understand. Please could you repeat"
        return question(speech_text).simple_card('HelloWorld',speech_text)
    speech_text = strftime("%H:%M",gmtime()) + " ;would you like to know the date"
    return question(speech_text).simple_card('HelloWorld',speech_text)
@ask.intent('WhereIntent')
def where():
    f = urllib2.urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    location_country = location['country_name']
    return question("You are in {}".format(location_country))

@ask.intent('AMAZON.HelpIntent')
def help():
	speech_text = 'You can say hello to me!'
	return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
	return "{}", 200


if __name__ == '__main__':
	app.run(debug = True)
