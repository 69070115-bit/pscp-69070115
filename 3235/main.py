"""fatty"""
amount = int(input())
bunny = []

for _ in range(amount):
    name, weight = input().split()
    weight = int(weight)
    bunny.append([name, weight])

fat_count = 0
max_weight = 0
max_name = ""

for name, weight in bunny:
    if weight > 15:
        fat_count += 1

    if weight > max_weight:
        max_weight = weight
        max_name = name

print(fat_count)
print(max_name)
