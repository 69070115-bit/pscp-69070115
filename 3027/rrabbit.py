"""RRABBIT"""

x,y,z = map(int, input().split())
price = int(input())

L = (2*x+2*y)*z
total=price*L

print(L)
print(total)
