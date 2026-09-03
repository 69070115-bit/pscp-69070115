""" Inflation"""
n = float(input())
k = int(input())

for _ in range(k):
    increase = n * 0.0381
    increase = int(increase * 100) / 100
    n += increase

print(f"{n:.2f}")
