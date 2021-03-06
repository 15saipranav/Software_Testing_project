import math
#This is a simple calculator program
class Application:
    def add(self,a,b):
        """This is addition method"""
        return a+b
    def sub(self,a,b):
        """This is subtraction method"""
        return a-b
    def mul(self,a,b):
        """This is multiplication method"""
        return a*b
    def div(self,a,b):
        """This is division method"""
        return a/b
    def sqrt(self,val):
        """This is square root method"""
        return math.sqrt(val)
    def log(self,val):
        """This is logarithm method"""
        return math.log10(val)
    def exp(self,base,power):
        """This is exponential method"""
        return math.pow(base,power)
