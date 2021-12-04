#Create a class called Rational for performing arithmetic with fractions. Write a program to test your class. Use integer variables to represent the private data of the class – the numerator and the denominator. Provide a __init__() method that enables an object of this class to be initialized when it’s declared. The __init__() should contain default parameter values in case no initializers are provided and should store the fraction in reduced form. For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator. Provide public methods that perform each of the following tasks:
#- printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
#- printing Rational numbers in floating-point format.

from math import gcd

class Rational:
    def __init__(self, numerator = 1, denominator = 2):
        self.__numerator = numerator / gcd(numerator, denominator);
        self.__denominator = denominator / gcd(numerator, denominator);
    def displayStandart(self):
        print(f'{int(self.__numerator)}/{int(self.__denominator)}');
    def displayFloating(self):
        print(f'{self.__numerator / self.__denominator}');

x = Rational(10,20);

x.displayStandart();

x.displayFloating();
