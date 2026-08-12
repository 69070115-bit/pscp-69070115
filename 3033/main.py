"""กระดาษ"""

x,y,z = map(int, input().split())
pi = 3.14

width = 2 * x + y
length = 2 * pi * x + z

print(f"{width:.2f} {length:.2f}")
