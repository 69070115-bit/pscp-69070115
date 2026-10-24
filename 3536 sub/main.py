"""isPrime_large"""

n = int(input())

if n < 2:
    print("NO")
else:
    prime = True
    i = 2

    while i * i <= n:
        if not n % i :
            prime = False
            break
        i += 1

    if prime:
        print("YES")
    else:
        print("NO")
