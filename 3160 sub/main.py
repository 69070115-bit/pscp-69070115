"""prime number"""
first, last = map(int, input().split())
primes = []
for n in range(first, last + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if not n % i:
            prime = False
            break

    if prime:
        primes.append(n)

if primes:
    print(*primes)

print(f"Total primes: {len(primes)}")
