"""gift and thief"""
n, k, t = map(int, input().split())
t -= 1
a = 0
c = 1
if a != t:
    for _ in range(n):
        tt = (a + k) % n
        if not tt:
            break
        c += 1
        a = tt
        if a == t:
            break
print(c)
