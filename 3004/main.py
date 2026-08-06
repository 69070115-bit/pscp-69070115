"""จุด3d"""

x1,y1,z1 = map(int, input().split())
x2,y2,z2 = map(int, input().split())
dx = (x1 - x2) ** 2
dy = (y1 - y2) ** 2
dz = (z1 - z2) ** 2
result = (dx + dy + dz) ** 0.5
print(f"{result:.2f}")
