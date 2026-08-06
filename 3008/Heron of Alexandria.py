"""Heron of Alexandria"""

a = float(input())
b = float(input())
c = float(input())

s = (a + b + c) /2

Area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print(f"{Area:.3f}")
