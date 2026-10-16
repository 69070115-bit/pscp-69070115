"""รหัสต้องไม่ซ้ำกัน"""
from collections import Counter

_ = int(input())
codes = list(map(int, input().split()))

count = Counter(codes)
result = sorted(x for x in count if count[x] == 1)

print(*result)
