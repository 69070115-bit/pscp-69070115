"""GAME"""
count = int(input())
points = 0
for _ in range(count):
    move = input()
    if move == "+":
        points += 10
    elif move == "-":
        points -= 5
print(points)
