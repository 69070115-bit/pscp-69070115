"""ลอดสะพาน"""

L, N = map(int, input().split())
bridges = []

for _ in range(N):
    a, b = map(int, input().split())
    bridges.append((a, b))

ans = 0

for x in range(L * 2 + 1):
    pos = x / 2
    count = 0

    for a, b in bridges:
        if a < pos < b:
            count += 1

    ans = max(ans, count)

print(ans)
