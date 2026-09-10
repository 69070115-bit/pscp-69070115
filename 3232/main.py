"""main"""
data = input().split()
x = int(data[0])
y = int(data[1])
total = 0
count = 0
jump = x

while jump > 0 and total < y:
    total = total + jump
    count = count + 1
    jump = jump - 2

if total >= y:
    print(count)
else:
    print(-1)
