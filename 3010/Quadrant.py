"""Quadrant"""

x = int(input())
y = int(input())

if not x and not y:
    print("O")
elif not y:
    print("X")
elif not x:
    print("Y")
elif x > 0:
    if y > 0:
        print("Q1")
    else:
        print("Q4")
else:
    if y > 0:
        print("Q2")
    else:
        print("Q3")
