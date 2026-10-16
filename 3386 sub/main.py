""" Duplicate I"""


m = int(input())
n = int(input())

group1 = set()

for _ in range(m):
    group1.add(int(input()))

ans = set()

for _ in range(n):
    x = int(input())
    if x in group1:
        ans.add(x)

if not ans:
    print("Nope")
else:
    for x in sorted(ans, reverse=True):
        print(x)
