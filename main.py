import logging
import os
from flask import Flask
import json
from flask_ask import Ask, request, session, question, statement
import math

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello(firstname):
    speech_text = "Hello %s" % firstname
    return statement(speech_text).simple_card('Hello', speech_text)

@ask.intent('MultiplyIntent', convert = {'a' :int, 'b' :int})
def multiply(a,b):
    c = a*b
    return question("{} multiplied by {} equals {}".format(a,b,c)).simple_card("Product","{} multiplied by {} equals {}".format(a,b,c))

@ask.launch
def law():
    return question("Please give be three values. The first value needs to be the coefficient of x squared. The second value needs to be the coefficient of x and the third value needs to be the constant term.").simple_card()
@ask.intent('QuadraticSolverThreeVarIntent', convert = {'a' :int, 'b' :int, 'c' :int})
def quad_three_var_solve(a,b,c):
        positive_value = (((-1)*b)+(math.sqrt((b**2.0)-(4.0*a*c))))/(2.0*a)
        negative_value = (((-1)*b)-(math.sqrt((b**2.0)-(4.0*a*c))))/(2.0*a)
        return question("The positive root of {} x squared {} x and {} is {} and the negative root of {} x squared {} x and {} is {}".format(a,b,c,positive_value,a,b,c,negative_value))

@ask.launch
def prime_check():
    return question("What integer would you like me to run the prime number check")
@ask.intent('PrimeCheckIntent', convert = {'num' :int})
def is_prime(num):
    '''
    Better method of checking for primes.
    '''
    if num % 2 == 0 and num > 2:
        return question("{} is not a prime number".format(num)).simple_card("{} is not a prime number".format(num))
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return question("{} is not a prime number".format(num)).simple_card("{} is not a prime number".format(num))
    return question("{} is a prime number".format(num)).simple_card("{} is a prime number".format(num))

if __name__ == '__main__':
    app.run(debug = True)
