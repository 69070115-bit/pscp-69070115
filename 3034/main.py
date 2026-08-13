"""pod"""

N, K = map(int, input().split())
station = [0]*K
for _ in range(N):
    station[int(input())-1] += 1
print(N - min(station)*K)
