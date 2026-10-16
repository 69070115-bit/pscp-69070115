"""หั่นขนมปัง"""
W, H, M, N = map(int, input().split())
X = [0] + list(map(int, input().split())) + [W]
Y = [0] + list(map(int, input().split())) + [H]

widths = sorted([X[i + 1] - X[i] for i in range(M + 1)], reverse=True)
heights = sorted([Y[i + 1] - Y[i] for i in range(N + 1)], reverse=True)

largest = widths[0] * heights[0]
second = max(widths[1] * heights[0], widths[0] * heights[1])

print(largest, second)
