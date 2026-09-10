"""Inflation"""
price = int(float(input()) * 100)
time = int(input())
i = 381
for _ in range(time):
    price += (price * i) // 10000
print(f"{price // 100}.{price % 100:02d}")
