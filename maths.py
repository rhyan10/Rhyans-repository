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
from Classes import calculus,functions,ApiConnect
cal = calculus()
connect = ApiConnect()
func = functions()

@ask.intent('IndefiniteIntIntegralIntent',convert={'a':int, 'b':int, 'c':int, 'd':int, 'e':int})
def integrate(a,b,c,d,e):
    speech_text = cal.Integralindef(a,b,c,d,e)
    return question(speech_text)

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
     return question("{} divided by {} equals {}".format(a,b,c))
@ask.intent('TweetIntent')
def calltweet(name):
    newname = name.lower().replace(" ","")
    print(newname)
    tweet = connect.twitterconnect(newname)
    return question("The most recent tweet from {} is : {}".format(name,tweet))
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
       speech_text = "Hello there"
       print a
       return question(speech_text).simple_card("Hello word", speech_text)

@ask.intent("AMAZON.NoIntent")
def nointent():
        speech_text = "sorry i didn't get what you said"
        return question(speech_text)
    # pass
@ask.session_ended
def session_ended():
	return "{}", 200


if __name__ == '__main__':
	app.run(debug = True)
