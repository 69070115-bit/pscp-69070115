"""นก"""

n = int(input())
h = list(map(int, input().split()))

count = 0

for i in range(n):
    if not i:
        if h[i] > h[i + 1] if n > 1 else True:
            count += 1
    elif i == n - 1:
        if h[i] > h[i - 1]:
            count += 1
    else:
        if h[i] > h[i - 1] and h[i] > h[i + 1]:
            count += 1

print(count)
