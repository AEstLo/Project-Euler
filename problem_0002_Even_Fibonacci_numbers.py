# Even Fibonacci numbers
# https://projecteuler.net/problem=2
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

import unittest


def sumFibo(num):
    if num < 2:
        return 0
    total = 2
    a = 1
    b = 2
    c = 3
    while c < num:
        if c % 2 == 0:
            total += c
        a = b
        b = c
        c = a + b
    return total


class Testing(unittest.TestCase):

    def test_main_test(self):
        self.assertEqual(sumFibo(10), 10)
        self.assertEqual(sumFibo(100), 44)
        self.assertEqual(sumFibo(200), 188)
        self.assertEqual(sumFibo(1000), 798)


if __name__ == '__main__':
    unittest.main()
