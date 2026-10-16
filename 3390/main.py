"""Array 2D ตรวจสอบ"""
a = [list(map(int, input().split())) for _ in range(5)]

row = [i for i in range(5) if sum(a[i]) % 2]
col = [j for j in range(5) if sum(a[i][j] for i in range(5)) % 2]

if row and col:
    print(row[0], col[0])
else:
    print(-1, -1)
