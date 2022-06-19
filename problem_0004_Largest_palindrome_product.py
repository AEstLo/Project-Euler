# Largest palindrome product
# https://projecteuler.net/problem=4
# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import unittest


def isPalindrome(num):
    n = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    return n == rev


def getLargestPalindromeProduct(upper_bound=None):
    if not upper_bound:
        upper_bound = 999 * 999
    assert 101101 < upper_bound < 1000000

    largest_palindrome = 101101
    for smaller in range(101, 1000):
        for bigger in range(smaller, 1000):
            prod = smaller * bigger
            if prod > upper_bound:
                break
            if largest_palindrome < prod and isPalindrome(prod):
                largest_palindrome = prod

    return largest_palindrome


class Testing(unittest.TestCase):

    def test_isPalindrome(self):
        self.assertEqual(isPalindrome(9), True)
        self.assertEqual(isPalindrome(101101), True)
        self.assertEqual(isPalindrome(101102), False)
        self.assertEqual(isPalindrome(131135), False)
        self.assertEqual(isPalindrome(531135), True)
        self.assertEqual(isPalindrome(5317135), True)
        self.assertEqual(isPalindrome(800000), False)
        self.assertEqual(isPalindrome(103401), False)
        self.assertEqual(isPalindrome(1000004000004000001), True)

    def test_main_test(self):
        self.assertEqual(getLargestPalindromeProduct(101102), 101101)
        self.assertEqual(getLargestPalindromeProduct(800000), 793397)
        self.assertEqual(getLargestPalindromeProduct(), 906609)


if __name__ == '__main__':
    unittest.main()
