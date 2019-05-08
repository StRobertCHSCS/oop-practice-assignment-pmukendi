"""
---------------------------------------------------------
Name: fraction.py
Purpose: creates fractions and performs operations on them

Author: Fabro.E and Phil.M
Created: 23/03/2019
---------------------------------------------------------
"""


class Fraction(object):

  def __init__(self, numerator, denominator):

    if denominator == 0:
      raise ValueError()
    else:
      self.numerator = numerator
      self.denominator = denominator

  def get_numerator(self):
    return self. numerator

  def get_denominator(self):
    return self.denominator

  def set_numerator(self, new_numerator):
    self.numerator = new_numerator

  def set_denominator(self, new_denominator):
    if new_denominator == 0:
      raise ValueError()
    else:
      self.denominator = new_denominator

  def __str__(self):
    self.__reduce()
    return str(int(self.numerator)) + "/" + str(int(self.denominator))

  def add(self, otherFraction):
    if self.denominator == otherFraction.denominator:
      self.numerator += otherFraction.numerator

    else:
      self.numerator *= otherFraction.denominator
      otherFraction.numerator *= self.denominator
      self.denominator *= otherFraction.denominator
      self.numerator += otherFraction.numerator

  def subtract(self, otherFraction):
    if self.denominator == otherFraction.denominator:
      self.numerator -= otherFraction.numerator
    else:
      self.numerator *= otherFraction.denominator
      otherFraction.numerator *= self.denominator
      self.denominator *= otherFraction.denominator
      self.numerator -= otherFraction.numerator

  def multiply(self, otherFraction):
    self.numerator = self.numerator * otherFraction.numerator
    self.denominator = self.denominator * otherFraction.denominator

  def __reduce(self):

    a = self.numerator
    b = self.denominator

    if abs(a) <= b:
      while a > 1:
        if self.numerator % a == 0 and self.denominator % a == 0:
          self.numerator /= a
          self.denominator /= a
          break
        else:
          a -= 1
    else:
      while b > 1:
        if self.numerator % b == 0 and self.denominator % b == 0:
          self.numerator /= b
          self.denominator /= b
          break
        else:
          b -= 1

if __name__ == '__main__':
  nume1 = int(input("Enter the first numerator: "))
  denom1 =  int(input("Enter the first denominator: "))
  nume2 = int(input("Enter a second numerator: "))
  denom2 = int(input("Enter a second denomiator: "))

  display1 = Fraction(nume1, denom1)
  display2 = Fraction(nume2, denom2)

  for i in range(3):
    fraction1 = Fraction(nume1, denom1)
    fraction2 = Fraction(nume2, denom2)

    if i == 0:
      fraction1.add(fraction2)
      print(display1, " + ", display2, " = ", fraction1)
    elif i == 1:
      fraction1.subtract(fraction2)
      print(display1, " - ", display2, " = ", fraction1)
    else:
      fraction1.multiply(fraction2)
      print(display1, " * ", display2, " = ", fraction1)
