'''
Kellie Poole
CMPS 2143 - OOP
Homework 1: Overload Add Method
'''

from fractions import gcd
'''Using code to find GCD from the standard library'''

class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def __add__(self,rhs):
        """
        @function: __add__
        @description: Overloads the Add Method; Reduces fraction; Fixes improper fraction, if needed
        @returns: Reduced solution to adding two fractions
        """ 
        x = self.numerator * rhs.denominator + self.denominator * rhs.numerator
        y = self.denominator * rhs.denominator
        simple = gcd(x,y)
        simplex = x//simple
        simpley = y//simple
        if simplex > simpley:
            a = simplex // simpley
            b = simplex % simpley
            if b == 0:
                return('%d' % (a))
            else:
                return('%d %d/%d' % (a,b,simpley))
        else:
            return fraction(x, y)

if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a + b
    print(c)
