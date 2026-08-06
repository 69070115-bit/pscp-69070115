"""coke"""

price = int(input())
pro_cap = int(input())
pro_price = int(input())
buy = int(input())

caps = 0
cost = 0

for _ in range(buy):
    _ += 0
    if 0 < pro_cap <= caps:
        cost += pro_price
        caps -= pro_cap
    else:
        cost += price

    caps += 1

print(cost)
