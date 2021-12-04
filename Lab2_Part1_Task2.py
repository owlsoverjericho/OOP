from math import gcd

class Rational:
    def __init__(self, numerator = 1, denominator = 2):
        self.__numerator = numerator / gcd(numerator, denominator);
        self.__denominator = denominator / gcd(numerator, denominator);
    def displayStandart(self):
        print(f'{int(self.__numerator)}/{int(self.__denominator)}');
    def displayFloating(self):
        print(f'{self.__numerator / self.__denominator}');
    def addition():
        pass
    def substraction():
        pass
    def multiplication():
        pass
    def division():
        pass

x = Rational(10,20);

x.displayStandart();

x.displayFloating();
