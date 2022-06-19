# Largest prime factor
# https://projecteuler.net/problem=3
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import unittest


def isPrime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def getNextPrime(num):
    i = num + 1
    while not isPrime(i):
        i += 1
    return i


def getLargestPrimerFactor(num):
    if num < 2:
        return 0

    i = 2
    while i * i <= num:
        if num % i == 0:
            num //= i
        else:
            i += 1

    return num


class Testing(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertEqual(isPrime(3), True)
        self.assertEqual(isPrime(7), True)
        self.assertEqual(isPrime(30), False)
        self.assertEqual(isPrime(14), False)
        self.assertEqual(isPrime(144), False)

    def test_get_next_prime(self):
        self.assertEqual(getNextPrime(3), 5)
        self.assertEqual(getNextPrime(7), 11)
        self.assertEqual(getNextPrime(30), 31)
        self.assertEqual(getNextPrime(14), 17)
        self.assertEqual(getNextPrime(144), 149)

    def test_main_test(self):
        self.assertEqual(getLargestPrimerFactor(10), 5)
        self.assertEqual(getLargestPrimerFactor(17), 17)
        self.assertEqual(getLargestPrimerFactor(49), 7)
        self.assertEqual(getLargestPrimerFactor(13195), 29)
        self.assertEqual(getLargestPrimerFactor(13195), 29)
        self.assertEqual(getLargestPrimerFactor(600851475143), 6857)
        self.assertEqual(getLargestPrimerFactor(25698751364526), 328513)


if __name__ == '__main__':
    unittest.main()
