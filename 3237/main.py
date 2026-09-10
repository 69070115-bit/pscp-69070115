"""triangle"""
n = int(input())

for row in range(n):
    for col in range(row + 1):
        if not col or row == n - 1 or row == col:
            print(0, end="")
        else:
            print(1, end="")
    print()
