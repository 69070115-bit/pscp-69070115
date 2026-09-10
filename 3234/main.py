"""decoration"""
start, amount = input().split()
amount = int(amount)
color = ["Red", "Green", "Blue"]

if start == "R":
    for i in range(0, amount):
        print(color[i % 3], end=" ")
elif start == "G":
    for i in range(0, amount):
        print(color[(i + 1) % 3], end=" ")
elif start == "B":
    for i in range(0, amount):
        print(color[(i + 2) % 3], end=" ")
