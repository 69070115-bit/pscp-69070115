"""Tuple's Sad life"""
t = tuple(input().split())
x = input()

pos = t.index(x)
n = t.count(x)

for _ in range(n):
    print(" ".join([str(pos)] * n))
