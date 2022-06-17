# Multiples of 3 or 5
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import unittest


def getSum(n):
    def getSumMultiples(num, numMultiples):
        return (num * numMultiples * (numMultiples + 1) // 2)
    threes = (n - 1) // 3
    fives = (n - 1) // 5
    fifteens = (n - 1) // 15
    return getSumMultiples(3, threes) + getSumMultiples(5, fives) - getSumMultiples(15, fifteens)


class Testing(unittest.TestCase):

    def test_main_test(self):
        self.assertEqual(getSum(10), 23)
        self.assertEqual(getSum(49), 543)
        self.assertEqual(getSum(100), 2318)
        self.assertEqual(getSum(1000), 233168)
        self.assertEqual(getSum(8456), 16687353)
        self.assertEqual(getSum(19564), 89301183)


if __name__ == '__main__':
    unittest.main()
