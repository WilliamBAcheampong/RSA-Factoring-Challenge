# rsa.py

import sys
import time

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize_rsa_number(n):
    for i in range(2, n):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i

def rsa_challenge(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for num in numbers:
        p, q = factorize_rsa_number(num)
        print(f"{num}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file>")
        sys.exit(1)

    start_time = time.time()
    rsa_challenge(sys.argv[1])
    end_time = time.time()

    print("\nTime taken:", round(end_time - start_time, 3), "seconds")
