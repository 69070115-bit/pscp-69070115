"""BusStop I"""
p = int(input())
n = int(input())
bus = []
count = 0

for _ in range(n):
    data = list(map(int, input().split()))
    stop = data[0]

    count += bus.count(stop)
    bus = [x for x in bus if x != stop]

    for dest in data[1:]:
        if dest > stop and len(bus) < p:
            bus.append(dest)

print(count)
