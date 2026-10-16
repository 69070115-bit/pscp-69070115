"""ไฟส่อง"""
n = int(input())
lights = []

for _ in range(n):
    a, b = map(int, input().split())

    if a < b:
        lights.append((a, b))
    else:
        lights.append((a, 360))
        lights.append((0, b))

lights.sort()

merged = []

for a, b in lights:
    if merged and a <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], b)
    else:
        merged.append([a, b])

if len(merged) == 1 and merged[0] == [0, 360]:
    print(360)
else:
    longest = 0

    for a, b in merged:
        longest = max(longest, b - a)

    if len(merged) > 1 and not merged[0][0]  and merged[-1][1] == 360:
        longest = max(
            longest,
            merged[0][1] + (360 - merged[-1][0])
        )

    print(longest)
