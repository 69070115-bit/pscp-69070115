"""sumofnumber"""
n = int(input())
s = 0

while True:
    x = int(input())

    if x == -1:
        break

    s += x

    if s == n:
        break

print(s)
