"""ส่งต่อ"""

N, S = map(int, input().split())

students = [0] * (N + 1)

for i in range(1, N + 1):
    students[i] = int(input())

visited = set()
current = S

while current and current not in visited:
    visited.add(current)
    current = students[current]

print(len(visited))
