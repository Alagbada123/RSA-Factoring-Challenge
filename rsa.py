import sys
import math

def is_prime(n):
    """ Check if a number is prime """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_factors(n):
    """ Find two prime factors p and q where n = p * q """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return (i, n // i)
    return (n, 1)  # If no prime factors found, return n and 1

def process_file(filename):
    """ Process the file and factorize the RSA number """
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        p, q = find_prime_factors(n)
        print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    process_file(filename)
