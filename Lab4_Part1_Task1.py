from math import gcd

class Rational:
    def __init__(self, numerator = 1, denominator = 2):
        self.__numerator = int(numerator / gcd(numerator, denominator));
        self.__denominator = int(denominator / gcd(numerator, denominator));
    def displayStandart(self):
        print(f'{int(self.__numerator)}/{int(self.__denominator)}');
    def displayFloating(self):
        print(f'{self.__numerator / self.__denominator}');
    def __add__(self, other):
        Anumerator = self.__numerator * other.__denominator
        Bnumerator = other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        result = Rational((Anumerator + Bnumerator), (denominator))
        return result
    def __sub__(self, other):
        Anumerator = self.__numerator * other.__denominator
        Bnumerator = other.__numerator * self.__denominator
        result = Rational((Anumerator - Bnumerator), (self.__denominator * other.__denominator))
        return result       
    def __mul__(self, other):
        result = Rational((self.__numerator * other.__numerator), (self.__denominator * other.__denominator))
        return result
    def __truediv__(self, other):
        result = Rational((self.__numerator * other.__denominator), (self.__denominator * other.__numerator))
        return result
    #Different comparisons
    def __eq__(self, other):
        if (self.__numerator == other.__numerator and self.__denominator == other.__denominator):
            return True
        else:
            return False
    def __ne__(self, other):
        if (self.__numerator != other.__numerator and self.__denominator != other.__denominator):
            return True
        else:
            return False
    def __lt__(self, other):
        if (self.__numerator < other.__numerator and self.__denominator < other.__denominator):
            return True
        else:
            return False
    def __gt__(self, other):
        if (self.__numerator > other.__numerator and self.__denominator > other.__denominator):
            return True
        else:
            return False
    def __le__(self, other):
        if (self.__numerator <= other.__numerator and self.__denominator <= other.__denominator):
            return True
        else:
            return False
    def __ge__(self, other):
        if (self.__numerator >= other.__numerator and self.__denominator >= other.__denominator):
            return True
        else:
            return False

x = Rational(5,8)
y = Rational(1, 5)
z = x + y
z.displayStandart()
print(x < y)
z.displayFloating()
