#!/usr/bin/env python3

import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorize_rsa(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return n, 1  # If no prime factors found

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
