# factors.py

import sys
import time

def factorize_number(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for num in numbers:
        p, q = factorize_number(num)
        print(f"{num}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    start_time = time.time()
    factorize_file(sys.argv[1])
    end_time = time.time()

    print("\nTime taken:", round(end_time - start_time, 3), "seconds")
