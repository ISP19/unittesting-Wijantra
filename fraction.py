import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.
    Fractions are always stored in proper form, without common factors in
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        self.check_inf = False
        self.check_nan = False

        # check that numerator and denominator is int or not
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("type object cannot be interpreted as an integer")

        else:
            if (numerator == 0 and denominator  == 0):  # 0/0 represent NaN
                self.numerator = 0
                self.denominator = 0
                self.check_nan = True
            elif (numerator == 1 and denominator == 0):  # 1/0 is infinity
                self.check_inf = True
                self.numerator = 1
                self.denominator = 0

            elif (numerator == -1 and denominator == 0):  # -1/0 is infinity
                self.check_inf = True
                self.numerator = -1
                self.denominator = 0

            elif denominator == 0:
                self.numerator = 1
                self.denominator = 0

            if math.gcd(numerator, denominator) == 1 and (self.check_nan == False) and (self.check_inf == False):
                if ('-' in str(denominator)):
                    self.numerator = numerator * -1
                    self.denominator = denominator * -1
                else:
                    self.numerator = numerator
                    self.denominator = denominator

            elif (self.check_nan == False) and (self.check_inf == False):
                if ('-' in str(denominator)):
                    self.numerator = (numerator * -1) / math.gcd(numerator,denominator)
                    self.numerator = int(self.numerator)
                    self.denominator = (denominator * -1) / math.gcd(numerator,denominator)
                    self.denominator = int(self.denominator)
                else:
                    self.numerator = numerator / math.gcd(numerator, denominator)
                    self.numerator = int(self.numerator)
                    self.denominator = denominator / math.gcd(numerator, denominator)
                    self.denominator = int(self.denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
        Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if (self.numerator == 0 and self.denominator == 0) or (frac.numerator == 0 and frac.denominator == 0):
            numerator = 0
            denominator = 0

        else:
            if (self.numerator == 1 and self.denominator == 0) or (frac.numerator == 1 and frac.denominator == 0):
                if self.numerator == -1 or frac.numerator == -1:
                    numerator = 0
                    denominator = 0
                else:
                    numerator = 1
                    denominator = 0
            else:
                numerator = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
                denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)


    def __mul__(self, frac):
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)


    def __str__(self):
        if self.denominator == 1 or self.denominator == -1:
            if '-' in str(self.denominator):
                return "-{:.0f}".format(self.numerator)
            return "{:.0f}".format(self.numerator)
        if '-' in str(self.denominator):
            return "-{:.0f}/{:.0f}".format(self.numerator, self.denominator * -1)
        return "{:.0f}/{:.0f}".format(self.numerator, self.denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
        Fractions are stored in proper form so the internal representation
        is unique (3/6 is same as 1/2).
        """
        """Two persons are qual if they have the same name"""

        if not isinstance(frac, Fraction):
            return False
        if (self.denominator == 0 and self.numerator == 0) and (frac.numerator == 0 and frac.denominator == 0):
            return True
        elif (self.denominator == 0 and self.numerator == 0) or (frac.numerator == 0 and frac.denominator == 0):
            return False
        if self.denominator == 0 or frac.denominator == 0:
            if self.numerator == frac.numerator:
                return True
            else:
                return False
        return (self.numerator / self.denominator) == (frac.numerator / frac.denominator)

