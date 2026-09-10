"""game"""
base = int(input())
bonus = int(input())
days = int(input())
multiplier = 1

if days > 3:
    multiplier = 1.5

sum_points = int((base + bonus) * multiplier)

if sum_points >= 1500:
    r = 5
elif sum_points >= 1000:
    r = 4
elif sum_points >= 500:
    r = 3
elif sum_points >= 200:
    r = 2
else:
    r = 1

if r == 5 and days >= 7:
    badge = 99
elif r == 4 and bonus > 300:
    badge = 88
else:
    badge = 0

print(sum_points)
print(r)
print(badge)
