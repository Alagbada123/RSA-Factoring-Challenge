#!/usr/bin/env python3

import sys
import random
from math import gcd

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

def factorize(n):
    if n == 1:
        return [1]

    factor = pollard_rho(n)
    if factor is None:
        return [n]

    return factorize(factor) + factorize(n // factor)

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                n = int(line.strip())
                factors = factorize(n)
                if len(factors) == 1:
                    print(f"{n}={n}*1")
                else:
                    p = factors[0]
                    q = n // p
                    print(f"{n}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid number in the file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    main(sys.argv[1])
