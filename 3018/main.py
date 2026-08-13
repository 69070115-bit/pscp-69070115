
"""rectangle"""
Ax,Ay,Aw,Ah = map(int,input().split())
Bx,By,Bw,Bh = map(int,input().split())

x = max(0,min(Ax+Aw,Bx+Bw) - max(Ax,Bx))
y = max(0,min(Ay+Ah,By+Bh) - max(Ay,By))

area = x*y
if area > 0:
    print(area)
else:
    print("no overlapping")
