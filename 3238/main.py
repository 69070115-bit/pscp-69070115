"""elon"""
x, k = input().split()
x = int(x)

middle = x // 2

for row in range(x):
    for col in range(x):
        if row == col or row + col == x - 1:
            if k == "#":
                print("#", end="")
            else:
                letter = chr(ord(k) + abs(row - middle))
                print(letter, end="")
        else:
            print("-", end="")
    print()
