"""Easy Histogram"""

s = input()

for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if c in s:
        print(f"{c} = {s.count(c)}")
