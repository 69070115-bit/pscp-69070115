"""แซงรอบ"""
n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

fastest = min(s)
count = sum((k - 1) * t < k * fastest for t in s)

print(count)
