"""ประสาท"""
import math
n_room = int(input())
if n_room == 1:
    R = 1
else:
    R = math.isqrt(n_room - 1) + 1

k = n_room - (R - 1) ** 2
if k % 2 == 1:
    walls = 2 * (R - 1)
else:
    walls = 2 * (R - 1) - 1
print(walls)
