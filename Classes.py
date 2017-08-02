import scipy as sc
import sympy as sp
x = sp.Symbol('x')
class functions:
    def createfunctions(self,a,b,c,d,e):
        function = None
        i = 0
        parameterlist = [a,b,c,d,e]
        for i in parameterlist:
            if  i == None:
                pass
            else:
                if i == 0:
                    function = a * x** 4
                elif i == 1:
                    function = function + b * x **3
                elif i == 2:
                    function = function + c * x **2
                elif i ==3:
                    function = function + d * x
                else:
                    function = function + e
        #if (b == None and c == None and d == None and e == None):
            #return a
        #elif(c == None and d == None and e == None):
            #return a * x + b
        #elif(b == None and d ==None and e == None):
            #return a* x**2 +
        #elif(d == None and e == None):
            #return a * x**2 + b * x + c
        #elif(e == None):
            #return a * x**3 + b * x**2 + c * x + d
        #else:
            #return a * x**4 + b * x**3 + c * x**2 + d * x + e
class calculus():
    def Integralindef(self,a,b,c,d,e):
        if (b is None and c is None and d is None and e is None):
            return("The integral of {} is {} x".format(a,a))
        elif(c == None and d == None and e == None):
            return("The integral of {} x plus {} is {} x squared plus {} x plus c".format(a,b,a/2,b))
        elif(d == None and e == None):
            return("The integral of {} x squared plus {} x plus {} is {} x cubed plus {} x squared plus {} x plus c ".format(a,b,c,a/3,b/2,c))
        elif(e == None):
            return("The integral of {} x cubed plus {} x squared plus {} x plus {} is {} x to the power of 4 plus {} x cubed plus {} x squared plus {} x + c ".format(a,b,c,d,a/4,b/3,c/2,d))
        else:
            return("The integral of {} x to the power of 4 plus {} x cubed plus {} x squared plus {} x plus {} is {} x to the power of 5 plus {} x to the power of 4 plus {} x cubed plus {} x squared plus {} x + c ".format(a,b,c,d,e,a/5,b/4,c/3,d/2,e))
    def differential(self,a,b,c,d,e):
        if (b == None and c == None and d == None and e == None):
            return("The derivative of {} is 0".format(a))
        elif(c == None and d == None and e == None):
            return("The derivative of {} x plus {} is {}".format(a,b,a))
        elif(d == None and e == None):
            return("The derivative of {} x squared plus {} x plus {} is {} x plus {}  ".format(a,b,c,2*a    ,b))
        elif(e == None):
            return("The derivative of {} x cubed plus {} x squared plus {} x plus {} is {} x squared plus {} x plus {} ".format(a,b,c,d,3*a,2*b,c))
        else:
            return("The derivative of {} x to the power of 4 plus {} x cubed plus {} x squared plus {} x plus {} is {} x cubed plus {} x squared plus {} x plus {} ".format(a,b,c,d,e,4*a,3*b,2*c,d))
    def areacurve(self,f,start,finish):
        sc.inte
class ApiConnect():
    def twitterconnect():
        Access_token = "892739265205063681-Og2W5jBCIZVKITrWILQhGc5ewiwHNFP"
        Access_secret = "OdeTww1bslkbYjYaloeoZZQgpI1EVl6HoWpSkcxrYsNLx"
        consumer_key = "61WsI5K9XqwxbD0qbMI585IzL"
        consumer_secret = "FfxurEbL9jZGfVBhopuSTqpGVWiC7HAxWaxoIXmxo68aeKPR0Y"
        
