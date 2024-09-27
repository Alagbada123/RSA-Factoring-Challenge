#!/usr/bin/env python3

import sys
import random
from math import gcd, sqrt

def pollard_rho(n):
    if n % 2 == 0:
        return 2

    def f(x):
        return (x * x + 1) % n

    x = random.randint(1, n-1)
    y = x
    d = 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d == n:
        return None
    else:
        return d

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorize_rsa(n):
    if is_prime(n):
        return n, 1

    factor = pollard_rho(n)
    if factor is None:
        return n, 1

    if is_prime(factor) and is_prime(n // factor):
        return factor, n // factor

    # If we haven't found two prime factors, continue factoring
    p = factorize_rsa(factor)[0]
    q = n // p
    return p, q

def main(filename):
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            p, q = factorize_rsa(n)
            print(f"{n}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid number in the file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)
    main(sys.argv[1])
