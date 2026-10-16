"""เข้าแถว"""
_, _ = map(int, input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in a:
    tallest = max(h[:i - 1], default=0)
    print(max(0, tallest - h[i - 1] + 1))
