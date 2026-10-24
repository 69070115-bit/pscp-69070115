"""B - Fully pair?"""

s = input()
count = {}
result = ""

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in s:
    if count[ch] % 2 == 1 and ch not in result:
        result += ch

if result:
    print(result)
else:
    print("fully paired")
