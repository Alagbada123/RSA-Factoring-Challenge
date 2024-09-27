import sys
import math

def factorize(n):
    """ Factorize a number into two factors p and q where n = p * q """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return (i, n // i)
    return (n, 1)  # For prime numbers or numbers that can't be factored into two smaller numbers

def process_file(filename):
    """ Process the file and factorize each number """
    with open(filename, 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    process_file(filename)
