"""Cave Explorer"""
n = int(input())
cave = list(map(int, input().split()))
s = input()

pos = cave.index(1)
treasure = cave.index(2)

for move in s:
    nxt = pos + (1 if move == "R" else -1)

    if 0 <= nxt < n:
        pos = nxt

    if pos == treasure:
        break

cave[cave.index(1)] = 0
cave[pos] = 1

print(*cave)
