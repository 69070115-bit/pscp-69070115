"""Milk"""

price = int(input())
pro_cap = int(input())
pro_buy = int(input())
money = int(input())

bottle_count = money // price
cap = bottle_count

if pro_cap > 0 and pro_buy > 0:
    while cap >= pro_cap:
        pro_bottle = (cap // pro_cap) * pro_buy
        bottle_count += pro_bottle
        cap = (cap % pro_cap) + pro_bottle

print(bottle_count)
