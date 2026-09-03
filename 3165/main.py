"""festival"""
move = input()
x = 0
y = 0
for i in move:
    if i == "N":
        y += 1
    elif i == "S":
        y -= 1
    elif i == "E":
        x += 1
    elif i == "W":
        x -= 1
    else:
        break

print(f"{x} {y} {abs(x) + abs(y)}")
