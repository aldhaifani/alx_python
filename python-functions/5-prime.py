#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers up to n.

    Args:
        n: The upper bound for the prime numbers.

    Returns:
        A list of prime numbers.
    """
    if n <= 1:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]


def is_prime(number):
    """
    Checks if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if the number is prime, False otherwise.
    """
    primes = sieve_of_eratosthenes(number)
    return number in primes
