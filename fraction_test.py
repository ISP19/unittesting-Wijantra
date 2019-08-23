import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__()) # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())
        f = Fraction(1, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-1, 0)
        self.assertEqual("-1/0", f.__str__())

    def test_init(self):
        f = Fraction(1, 3)
        self.assertEqual(1, f.numerator)
        self.assertEqual(3, f.denominator)
        f = Fraction(3)
        self.assertEqual(3, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(1, -1)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(3, 0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(4, -4)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(0, 1)
        self.assertEqual(0, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(25, 5)
        self.assertEqual(5, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(-32, 6)
        self.assertEqual(-16, f.numerator)
        self.assertEqual(3, f.denominator)
        f = Fraction(1, 0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(0, 0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(-1, 0)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)

        with self.assertRaises(TypeError):
            Fraction(9.9, 1)

        with self.assertRaises(TypeError):
            Fraction(9, 2.1)

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(2, 6), Fraction(1, 6) + Fraction(1, 6))
        self.assertEqual(Fraction(28, 45), Fraction(5, 9) + Fraction(6, 90))
        self.assertEqual(Fraction(11, 89), Fraction(-78, 89) + Fraction(1))
        self.assertEqual(Fraction(28, 45), Fraction(5, 9) + Fraction(6, 90))
        self.assertEqual(Fraction(-8), Fraction(-15, 3) + Fraction(6, -2))
        self.assertEqual(Fraction(33, 16), Fraction(800, 400) + Fraction(500,8000))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) + Fraction(1, 0))  # case that infinity plus infinity is inf
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) + Fraction(0, 0))  # case that infinity plus nan is nan
        self.assertEqual(Fraction(0, 0), Fraction(3, 3) + Fraction(0, 0))  # case that number plus nan is nan
        self.assertEqual(Fraction(0, 0), Fraction(-3, 3) + Fraction(0, 0))
        self.assertEqual(Fraction(1, 0), Fraction(0) + Fraction(1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) + Fraction(-1, 0))  # case that infinity - infinity is nan
        self.assertEqual(Fraction(1, 0), Fraction(3, 0) + Fraction(1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(-3, 0) + Fraction(1, 0))

    def test_mul(self):
        self.assertEqual(Fraction(5, 507), Fraction(1, 39) * Fraction(5, 13))
        self.assertEqual(Fraction(0), Fraction(0, 1) * Fraction(0))
        self.assertEqual(Fraction(5), Fraction(5, 1) * Fraction(1, 1))
        self.assertEqual(Fraction(-1, 4), Fraction(-2, 4) * Fraction(2, 4))
        self.assertEqual(Fraction(-789654, 13696857811), Fraction(3, 89999) * Fraction(789654, -456567))
        self.assertEqual(Fraction(5, 507), Fraction(1, 39) * Fraction(5, 13))
        self.assertEqual(Fraction(8), Fraction(8, 1) * Fraction(1))
        self.assertEqual(Fraction(1, 0), Fraction(1, 0) * Fraction(1, 0))
        self.assertEqual(Fraction(0, 0), Fraction(8, 4) * Fraction(0, 0))  # case that number multiply nan is nan
        self.assertEqual(Fraction(0, 0), Fraction(0) * Fraction(1, 0))  # case that 0 multiply infiny is nan
        self.assertEqual(Fraction(0, 0), Fraction(0) * Fraction(-1, 0))  # case that 0 multiply -infiny is nan
        self.assertEqual(Fraction(-1, 0),Fraction(1, 0) * Fraction(-1, 0))  # case that infinity multiply -infiny is -infinity

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)  # not quite 1/2
        m = Fraction(-3, -5)
        n = Fraction(6, 10)
        o = Fraction(0, 1)
        p = Fraction(0)
        q = Fraction(1, 0)
        r = Fraction(-3, 0)
        s = Fraction(-1, 0)
        u = Fraction(3, 0)
        v = Fraction(0, 0)

        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(m == n)
        self.assertTrue(m.__eq__(n))
        self.assertFalse(m == h)
        self.assertFalse(m.__eq__(h))
        self.assertTrue(o == p)
        self.assertTrue(o.__eq__(p))
        self.assertFalse(q == s)
        self.assertFalse(q.__eq__(s))
        self.assertFalse(r == u)
        self.assertFalse(r.__eq__(u))
        self.assertTrue(q == u)
        self.assertTrue(q.__eq__(u))
        self.assertFalse(p == v)  # 0 != 0/0 (Nan)
        self.assertFalse(p.__eq__(v))
        # Consider special values like 0, 1/0, -1/0
