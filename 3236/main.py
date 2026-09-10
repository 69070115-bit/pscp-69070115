"""son"""
n = int(input())
first = input()
second = input()

count = 0

for i in range(n):
    if int(first[i]) + int(second[i]) != 9:
        count += 1

if not count:
    print("YES")
else:
    print("NO", count)
