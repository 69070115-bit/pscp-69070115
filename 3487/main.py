"""ติดตั้งหลอดไฟ"""
n = int(input())
poles = [int(input()) for _ in range(n)]

poles.sort()

height = 0
total = 0

for pole in poles:
    height += pole
    total += height * 2

print(total)
